# ZTEdge URL Analyze

## Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)

## Introduction

This code will take a line-by-line text file of domain names and run it through [Ericom's ZTEdge platform](https://www.ericom.com) to perform URL analysis in bulk. The outcome will be a list of domains and their associated categories.

## Requirements

- Access to ZTAdmin portal
- ZTEdge API key
- Python3

```
git clone git clone https://github.com/JeffGiroux/ztedge-url-analyze.git
cd ztedge-url-analyze
pip3 install -r requirements.txt
```

## Usage

1. Format the domain/URL list into line-by-line text file. See [urls.txt](./urls.txt) for an example.

Example URL text file:
```
google.com
cnn.com
secure.eicar.org/eicar_com.zip
```

2. Execute python command.

Syntax:
```
python3 url_analyze.py <Tenant ID> <API Key> <URL-text-file>
```

Example:
```
python3 url_analyze.py 555-444-333-222-111 keyAAABBBCCC ./urls.txt
```

3. View results

Example Output:
```
Authenticating and retrieving token...
google.com,Search Engines/Portals -> Search Engines & Portals
cnn.com,News -> News
secure.eicar.org/eicar_com.zip,High Risk -> Miscellaneous
Done!
```