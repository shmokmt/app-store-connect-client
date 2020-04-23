# app store connect client

Python package for App Store Connect API.

It supports Python3.7+.

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
    'measures': app_store.measures.installs
}
query = Query.metrics(app_id, config).date('2016-04-01', '2016-04-02')
results = client.execute(query)
print(results, indent=4)
```

### response

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
* Support 2FA Authentication
* Docstring
* readthedocs
* Support Review API
* Use async / await
* group by method

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