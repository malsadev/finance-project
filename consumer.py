from kafka import KafkaConsumer
import sys
from json import dumps,loads
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


print(sys.argv)
subscribable_symbols = sys.argv[1:len(sys.argv)]
# subscribable_symbols = ",".join(subscribable_symbols)

print(subscribable_symbols)

consumer = KafkaConsumer(*subscribable_symbols,
                          bootstrap_servers=['44.202.82.167:9092'], #add your IP here
                          value_deserializer=lambda x: loads(x.decode('utf-8')))

plt.style.use('fivethirtyeight')

# for event in consumer:
#     print(event.value)

symbols = {}


def animate(i):

    # event = consumer.poll(max_records=1, timeout_ms=2000)

    # print(event)
    for event in consumer:
        msg_map = json.loads(event.value)

        symbol = msg_map["data"][0]["s"]

        if symbol not in symbols:
            symbols[symbol] = [[],[]]
    
        symbols[symbol][0].append(msg_map["data"][0]["t"])
        symbols[symbol][1].append(msg_map["data"][0]["p"])

        plt.cla()
        plt.plot(symbols[symbol][0], symbols[symbol][1], label=symbol)
        plt.legend(loc='upper left')
        plt.tight_layout()
        break



ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()


