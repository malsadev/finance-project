# import json
# import ast
# test_string = """{
#   "data": [
#     {
#       "p": 7296.89,
#       "c": null,
#       "s": "BINANCE:BTCUSDT",
#       "t": 1575526691134,
#       "v": 0.011467
#     }
#   ],
#   "type": "trade"
# }"""
# # BINANCE_BTCUSDT
# # test_dict = eval(test_string) // theows exception on nulls
# test_dict = json.loads(test_string) #// modifies null values to None, makes sense, best option
# # test_dict = ast.literal_eval(test_string) // many issues

# print(test_dict["type"])
# print(test_dict["data"])
# print(test_dict["data"][0]["s"])

# ch_replace_rules = {" ": "_", ":": "_"}
# for ch in ch_replace_rules.keys():
#     print(ch, "replaced with", ch_replace_rules[ch])
#     test_dict["data"][0]["s"].replace(ch, ch_replace_rules[ch])

# print(test_dict["data"][0]["s"])

# ticker_val = "APPl"
# ticker_subscription = '{"type":"subscribe","symbol":"%s"}' % ticker_val

# # ticker_subscription = f'{"type":"subscribe","symbol":{}}'.format(ticker=ticker_val)
# print("sending subscription", ticker_subscription)


# import random
# from itertools import count
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# plt.style.use('fivethirtyeight')

# x_vals = []
# y_vals = []

# index = count()


# def animate(i):
#     data = pd.read_csv('data.csv')
#     x = data['x_value']
#     y1 = data['total_1']
#     y2 = data['total_2']

#     plt.cla()

#     plt.plot(x, y1, label='Channel 1')
#     plt.plot(x, y2, label='Channel 2')

#     plt.legend(loc='upper left')
#     plt.tight_layout()


# ani = FuncAnimation(plt.gcf(), animate, interval=1000)

# plt.tight_layout()
# plt.show()

# import sys

# print(sys.argv)