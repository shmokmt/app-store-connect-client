# app store connect client

Python package for App Store Connect API.

![python_version](https://img.shields.io/pypi/pyversions/app-store-connect-client)   ![LICENSE](https://img.shields.io/pypi/l/app-store-connect-client)

It supports Python3.6.1+.

The complete documentation is [here](https://github.com/shmokmt/app-store-connect-client/wiki).

## Installation

```bash
pip install app-store-connect-client
```

## Getting Started

```python
import app_store_connect_client as app_store
import json


app_id = '12345'
client = app_store.Client(username="XXX", password="XXX)
# query config.
config = {
    'measures': [app_store.measures.installs]
}
query = app_store.Query(app_id).metrics(config).date('2016-04-01', '2016-04-02')
results = client.execute(query)
print(json.dumps(results, indent=4))
```

### results

```json
{
    "size": 1,
    "results": [
        {
            "adamId": "12345678",
            "meetsThreshold": true,
            "group": null,
            "data": [
                {
                    "date": "2020-04-01T00:00:00Z",
                    "installs": 50.0
                }
            ],
            "totals": {
                "value": 50.0,
                "type": "COUNT",
                "key": "installs"
            }
        }
    ]
}
```

## TODO
* More tests
* More Example
* More docs
* Support 2FA Authentication
* Docstring
* Support Review API
* Support group_by method
* Support filter_by method

## Credit

* [JanHalozan/iTunesConnectAnalytics](https://github.com/JanHalozan/iTunesConnectAnalytics)


## Related Projects

* [stoprocent/node-itunesconnect](https://github.com/stoprocent/node-itunesconnect)
* [JanHalozan/iTunesConnectAnalytics](https://github.com/JanHalozan/iTunesConnectAnalytics)
* [Donohue/itc_analytics](https://github.com/Donohue/itc_analytics)
* [simongcx/pytunesconnect](https://github.com/simongcx/pytunesconnect)
* [elyticscode/itc_analytics](https://github.com/elyticscode/itc_analytics)

## LICENSE

[MIT](https://github.com/shmokmt/app-store-connect-client/blob/master/LICENSE)


## Authors
* [shmokmt](https://github.com/shmokmt)