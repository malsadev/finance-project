from kafka import KafkaProducer
import pandas as pd
from time import sleep

from json import dumps
import json


producer = KafkaProducer(bootstrap_servers="52.20.5.51:9092",
                         value_serializer=lambda x:
                         dumps(x).encode("utf-8"))

# producer.send("demo_test", value="something"
              
df = pd.read_csv("indexProcessed.csv")
while True:
    msg = df.sample(1).to_dict(orient="records")[0]
    producer.send("stocks", value=msg)
    sleep(1)

