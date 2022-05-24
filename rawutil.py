import plotly.graph_objs as go
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(ticker,period):
    data = yf.download(tickers = ticker, 
                       period=period,
                       interval = '1d', 
                       progress = False, 
                       rounding= True
                       )
    data.reset_index()
    data['Date'] = pd.to_datetime(data['Date']).dt.date
    return data

def simple_line_graph(df):
    plt.figure(figsize = (18,9))
    plt.plot(range(df.shape[0]),(df['Low']+df['High'])/2.0)
    plt.xticks(range(0,df.shape[0],500),df['Date'].loc[::500],rotation=45)
    plt.xlabel('Date',fontsize=18)
    plt.ylabel('Mid Price',fontsize=18)
    plt.show()

def data_visualization(data, name):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data['Date'], 
                                 open = data['Open'], 
                                 high = data['High'], 
                                 low = data['Low'], 
                                 close = data['Close'], 
                                 name = 'market data'))
    fig.update_layout(title = name, yaxis_title = 'Stock Price (INR)')
    fig.update_xaxes(rangeslider_visible=True, 
                     rangeselector=dict( buttons=list(
                         [
                          dict(count=15, label='15m', step="minute", stepmode="backward"), 
                          dict(count=45, label='45m', step="minute", stepmode="backward"),
                          dict(count=1, label='6mo', step="month", stepmode="backward"), 
                          dict(count=6, label='1y', step="year", stepmode="backward"),
                          dict(step="all")
                          ]
                          )))
    fig.show()

