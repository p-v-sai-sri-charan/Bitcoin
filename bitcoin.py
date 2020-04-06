from requests import Request, Session
import requests
import pymongo
import datetime
import json
import schedule
import time
from datetime import timedelta
from matplotlib import pyplot
import pylab as pl
#import settings
client = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = client.list_database_names()
IFTTT_WEBHOOKS_URL= 'https://maker.ifttt.com/trigger/{}/with/key/eMTgQL8QHS3YbRdIAqq0eoPptSNmgMrj7LGTZoBz0ew?value1={}'

def get_bitcoin():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'dbd98a70-e837-41f5-b2d8-060221022ab5',
        }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data['data'][0]['quote']['USD']['price']
    print("Latest Bit Coin Price :",price)
    if price >= 6500 and price <=6000:
        event = 'bit_coin_price_emergency'
        event_url = 'https://maker.ifttt.com/trigger/{}/with/key/eMTgQL8QHS3YbRdIAqq0eoPptSNmgMrj7LGTZoBz0ew?value1={}'
        event_url_post = IFTTT_WEBHOOKS_URL.format(event,price)
        requests.post(event_url_post)
    return price

def insert_db():
    
    bit_coin_price = get_bitcoin()

    if "project3" in dblist:
        
        db = client["project3"]
        collist = db.list_collection_names()
        if "bitcoin" in collist:
            collection = db["bitcoin"]
            values = {"name": "Bitcoin",
                  "price":bit_coin_price,
                  "date":datetime.datetime.now(),
                  "symbol":"BTC"
                }
            save = collection.insert_one(values)
            
            telegram_update(bit_coin_price)
        else:
            collection = db["bitcoin"]
            insert_db()
    else:
        db = myclient['bitcoin']
        insert_db()

    telegram_update(bit_coin_price)
    graph()

def graph():
    db = client["project3"]
    collection = db["bitcoin"]
    myresult = collection.find()
    a=[]
    b= []
    for x in myresult:
        i = x['price']
        a.append(i)
        j = x['date'].strftime("%x")
        b.append(j)

    pl.plot(a,b)
    pl.show()

def telegram_update(bit_coin_price):
    event = 'bit_coin_telegram'
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event,bit_coin_price)
    requests.post(ifttt_event_url)


schedule.every(10).seconds.do(insert_db)
while True:
    schedule.run_pending()
    time.sleep(1)
