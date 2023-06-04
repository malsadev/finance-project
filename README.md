# finance-project

This is a distributed system that consumes real-time stock/crypto trades and plots the trade value in function of time. 
You will need to configure a kafka server to start this application.

To run the the producer,
  python producer.py <space seperated list of tickers>, this will consume the data for the provided tickers and publish them to kafka
  
To run the consumer,
  python consumer.py <space separated list of tickers>, this will plot the real-time data using a line chart for all the given tickers
