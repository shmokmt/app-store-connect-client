# app store connect client(WIP)

Python package for App Store Connect API.

It supports Python3.7+.

The complete documentation is here.

## Installation

```bash
pip install app-store-connect-client
```

## Getting Started

```python
from app_store_connect_client import Client, Query

app_id = '12345'
client = Client(username="XXX", password="XXX)

# Getting account informantion
client.get_apps()


# more setting info.
client.get_settings() 

# query
config = {
    'measures': itc.measures.units
}

query = Query.metrics(app_id, config).date('2016-04-10', '2016-05-10')

client.execute(query)
```

### Related Projects

* [stoprocent/node-itunesconnect](https://github.com/stoprocent/node-itunesconnect)
* [JanHalozan/iTunesConnectAnalytics](https://github.com/JanHalozan/iTunesConnectAnalytics)
* [Donohue/itc_analytics](https://github.com/Donohue/itc_analytics)
* [simongcx/pytunesconnect](https://github.com/simongcx/pytunesconnect)
* [elyticscode/itc_analytics](https://github.com/elyticscode/itc_analytics)

### LICENSE

MIT