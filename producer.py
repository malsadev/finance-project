
# producer = KafkaProducer(bootstrap_servers="52.20.5.51:9092",
#                          value_serializer=lambda x:
#                          dumps(x).encode("utf-8"))

# # producer.send("demo_test", value="something"
              
# df = pd.read_csv("indexProcessed.csv")
# while True:
#     msg = df.sample(1).to_dict(orient="records")[0]
#     producer.send("stocks", value=msg)
#     sleep(1)
#https://pypi.org/project/websocket_client/
import websocket
from kafka import KafkaProducer
from json import dumps
import json
import sys
from dotenv import load_dotenv
import os
load_dotenv()

API_TOKEN = os.environ.get("api-key")

producer = KafkaProducer(bootstrap_servers="44.202.82.167:9092",
                         value_serializer=lambda x:
                         dumps(x).encode("utf-8"))


ch_replace_rules = {" ": "_", ":": "_"}

def on_message(ws, message):
    print(message)
    msg_map = json.loads(message)

    # how to deal with pings 
    if msg_map["type"] == "ping": #ignnore pings
        return
    
    raw_symbol = msg_map["data"][0]["s"]
    publlishable_symbol = ""

    # character not a valid topic name, only a-z, A-Z, 0-9, . (dot), _ (underscore), and - (dash)
    for ch in ch_replace_rules.keys():
        publishable_symbol = raw_symbol.replace(ch, ch_replace_rules.get(ch))

    print("sending msg to topic:", publishable_symbol)
    producer.send(publishable_symbol, value=message) 
    
def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")
    ws.c

def on_open(ws): #max 50 symbol subscriptions on free plan, 30api/calls per second limit

    for ticker in range(1, len(sys.argv)): #what happens when len(sys.args) > 51
        ticker_val = sys.argv[ticker]
        ticker_subscription = ticker_subscription = '{"type":"subscribe","symbol":"%s"}' % ticker_val
        print("sending subscription", ticker_subscription)
        ws.send(ticker_subscription)

websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=%s" % API_TOKEN, #toke should be an env variable in a gitignored fie
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
# ws.enableTrace(True)
ws.on_open = on_open
try:
    ws.run_forever()
except Exception:
    ws.close()

