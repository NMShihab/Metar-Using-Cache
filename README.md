
# Metar

The National Weather Service is a part of the National Oceanic and Atmospheric Admininstration and is change of providing weather forecast and warning warning all around U.S. The station make ther data available over inernet in a specaioal format called Metar.

Our purpose is exract data and retun  latest searched data with a human readable format like:

METAR CODE: KSGS 171538Z 19005KT M01/M03 

Return : {"station":"KSGS","last_observation":"2001-11-17 15:38 GTM","temperature":"-1 C (30 F)","wind":"Wind direction is 190 degree, velocity is 05 knots"}


## Installation

Install python 3.7 or more.
For Install python[ Click here](https://www.python.org/downloads/macos/)

Install Redis. For details [Click here](https://redis.io/download)

Extract metar.tar.gz .Open terminal in metar file. Then use this command:

```bash
  yourpath/metar$ pip install -r requirements.txt
```
Then all requirements will be installed in your system.
Then use this command to run your project.
```bash
  yourpath/metar$ python manage.py runserver
```
Your Server will be run in [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

To check normal response go [http://127.0.0.1:8000/metar/ping](http://127.0.0.1:8000/metar/ping)

You will see response : {"data": "pong"}

Then,

Go This url [http://127.0.0.1:8000/metar/info/](http://127.0.0.1:8000/metar/info/)

Search with only station code and keep empty nocache field. You will get latest response from station code. If you search again with same station code data will come from cache. This cache data will remain 5 minitues.

If you want data from Database and clear the cache please search station field wit station code and nocache field with 1.

Your response will come from database and all cache data will be cleared.

You can also Search with Url: [http://127.0.0.1:8000/metar/info/?scode=&nocache=](http://127.0.0.1:8000/metar/info/?scode=&nocache=)

after scode= please give the station code and use nocache=1 if and only if you want your data come from database and cached hase been cleared otherwise keep that empty.

## Thank You