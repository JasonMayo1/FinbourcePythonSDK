![LUSID_by_Finbourne](./resources/Finbourne_Logo_Teal.svg)

# Python SDK for the LUSID API

## Contents

- [Summary](#summary)
- [Versions](#versions)
- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
    * [Environment variables](#environment-variables)
    * [Secrets file](#secrets-file)
    * [Example](#example)
- [Endpoints and models](#endpoints-and-models)

## Summary

This is the python SDK for the LUSID API, part of the [LUSID by FINBOURNE](https://www.finbourne.com/lusid-technology) platform. To use it you'll need a LUSID account - [sign up for free at lusid.com](https://www.lusid.com/app/signup).

LUSID is a bi-temporal investment management data platform with portfolio accounting capabilities - see https://support.lusid.com/knowledgebase/ to learn more.

For more details on other applications in the LUSID platform, see [Understanding all the applications in the LUSID platform](https://support.lusid.com/knowledgebase/article/KA-01787).

This sdk supports `Production`, `Early Access`, `Beta` and `Experimental` API endpoints. For more details on API endpoint categories, see [What is the LUSID feature release lifecycle](https://support.lusid.com/knowledgebase/article/KA-01786). To find out which category an API endpoint falls into, see the [swagger page](https://www.lusid.com/api/swagger/index.html).

This code is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project.

## Versions

- API version: 0.11.6765
- SDK version: 2.1.334

## Requirements

- Python 3.7+

## Installation

If using [poetry](https://python-poetry.org/docs/)

```
poetry add lusid-sdk
```

If using [pip](https://pypi.org/project/pip/)

```
pip install lusid-sdk
```

Then import the package in your python file
```python
import lusid
```

## Getting Started

You'll need to provide some configuration to connect to the LUSID API - see the articles about [short-lived access tokens](https://support.lusid.com/knowledgebase/article/KA-01654) and a [long-lived Personal Access Token](https://support.lusid.com/knowledgebase/article/KA-01774). This configuration can be provided using a secrets file or environment variables. 

### Environment variables

Required for a short-lived access token
``` 
FBN_TOKEN_URL
FBN_LUSID_URL
FBN_USERNAME
FBN_PASSWORD
FBN_CLIENT_ID
FBN_CLIENT_SECRET
```

Required for a long-lived access token
``` 
FBN_LUSID_URL
FBN_ACCESS_TOKEN
```

You can send your requests to the LUSID API via a proxy, by setting `FBN_PROXY_ADDRESS`. If your proxy has basic auth enabled, you must also set `FBN_PROXY_USERNAME` and `FBN_PROXY_PASSWORD`.

### Secrets file

The secrets file must be in the current working directory.

Required for a short-lived access token
```json
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "lusidUrl":"https://<your-domain>.lusid.com/api",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>",
    }
}
```

Required for a long-lived access token
```json
{
    "api":
    {
        "lusidUrl":"https://<your-domain>.lusid.com/api",
        "accessToken":"<your-access-token>"
    }
}
```

You can send your requests to the LUSID API via a proxy, by adding a proxy section. If your proxy has basic auth enabled, you must also supply a `username` and `password` in this section.

```json
{
    "api":
    {
        "lusidUrl":"https://<your-domain>.lusid.com/api",
        "accessToken":"<your-access-token>"
    },
    "proxy":
    {
        "address":"<your-proxy-address>",
        "username":"<your-proxy-username>",
        "password":"<your-proxy-password>"
    }
}
```

### Example
```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    AborApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "lusidUrl":"https://<your-domain>.lusid.com/api",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(AborApi)
        scope = 'scope_example' # str | The scope of the Abor.
        code = 'code_example' # str | The code of the Abor.
        diary_entry_code = 'diary_entry_code_example' # str | Diary entry code

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # diary_entry_request = DiaryEntryRequest()
        # diary_entry_request = DiaryEntryRequest.from_json("")
        diary_entry_request = DiaryEntryRequest.from_dict({"name":"2023_Q1","status":"Estimate","effectiveAt":"2023-04-02T15:10:10.0000000+00:00","queryAsAt":"2023-04-15T15:10:10.0000000+00:00","properties":{"DiaryEntry/AccountingDiary/Reports":{"key":"DiaryEntry/AccountingDiary/Reports","value":{"labelValue":"Some comments"}}}}) # DiaryEntryRequest | The diary entry to add.

        try:
            # [EXPERIMENTAL] AddDiaryEntry: Add a diary entry to the specified Abor.
            api_response = await api_instance.add_diary_entry(scope, code, diary_entry_code, diary_entry_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AborApi->add_diary_entry: %s\n" % e)

asyncio.run(main())
```


## Endpoints and models

- See [Documentation for API Endpoints](sdk/README.md#documentation-for-api-endpoints) for a description of each endpoint
- See [Documentation for Models](sdk/README.md#documentation-for-models) for descriptions of the models used

