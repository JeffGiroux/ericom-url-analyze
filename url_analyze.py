import requests
import json
import uuid, sys, time


def get_jwt(tenant, key):
    url = "https://ztadmin.ericomcloud.net/api/v1/auth"
    payload = json.dumps({
      "tenantID": tenant,
      "key": key
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    jwt = response.json()['JWT']
    cookie = response.cookies['route']
    return jwt, cookie

def logout(jwt):
    url = "https://ztadmin.ericomcloud.net/api/v1/auth"
    headers = {
      'Content-Type': 'application/json',
      'Authorization': (f'Bearer {jwt}')
    }
    response = requests.request("DELETE", url, headers=headers)
    return response

def analyze_urls(domainUrl,jwt,cookie):
    url = "https://ztadmin.ericomcloud.net/api/v1/policies/analyze"
    payload = json.dumps({
      "url": f'http://{domainUrl}'
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': (f'Bearer {jwt}'),
      'Cookie': 'route={0}'.format(str(cookie))
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    category_name = response.json().get('url', {}).get('categoryName')
    return category_name


def usage():
    print("Usage: python3 url_analyze.py <Tenant ID> <API Key> <URL-text-file>")

if __name__ == "__main__":
    
    try:
        auth_tenant = sys.argv[1]
    except:
        print("Tenant ID missing")
        usage()
        exit(1)
    try:
        key = sys.argv[2]
    except:
        print("API Key missing")
        usage()
        exit(1)
    try:
        urls = sys.argv[3]
    except:
        print("Text File missing")
        usage()
        exit(1)
    
    print("Authenticating and retrieving token...")
    jwt, cookie = get_jwt(auth_tenant, key)

    with open(urls, 'r') as file:
        for line in file:
            # Assuming each line contains values separated by a space
            values = line.strip().split()
            domainUrl = values[0]
            resp = analyze_urls(domainUrl,jwt,cookie)
            print(f'{domainUrl},{resp}')
    
    print("Done!")

    logout(jwt)

