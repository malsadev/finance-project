import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from kafka import KafkaConsumer


# requirements:

# 1.every day plot the latest 200 values of some stock ticker

    # 1.1 values could be of several types, open, close, high, low etc... for now stick to one type
    # 1.2 as a stretch goal, plot all of them on the same graph
    # 1.3 no need to save the graph

# 2.predict the values of the next five days (no need for them to be plotted) on console

    # 2.1 the n-last predicted values + the last  (historical values - n) will be taken into account to predict the current value

# 3. the stock data feed should be coming from a kafka topic published from producer application hitting the api endpoint

# 4. this plotting application is configurable to choose which stock tickers to plot and predict, displays as many line charts as needed
    # 4.1 the producer is also configured to choose which tickers to publish




# 5. to mimic real-time nature, the producer will publish one value at a time, then consumer integrates it into the graph and plots, and predict next 5 values



# 6. don't worry about what happens when a publisher or a consumer (plotter fails)



