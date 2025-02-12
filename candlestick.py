import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Generate sample stock data
np.random.seed(42)
df_stocks = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=30),
    'Open': np.random.normal(100, 10, 30),
    'High': np.random.normal(105, 10, 30),
    'Low': np.random.normal(95, 10, 30),
    'Close': np.random.normal(100, 10, 30)
})

# Ensure High is highest and Low is lowest
df_stocks['High'] = df_stocks[['Open', 'Close', 'High']].max(axis=1)
df_stocks['Low'] = df_stocks[['Open', 'Close', 'Low']].min(axis=1)

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df_stocks['Date'],
    open=df_stocks['Open'],
    high=df_stocks['High'],
    low=df_stocks['Low'],
    close=df_stocks['Close']
)])

fig.update_layout(
    title='Stock Price Analysis',
    yaxis_title='Stock Price',
    template='plotly_dark',
    xaxis_rangeslider_visible=True,
    width=800,
    height=600
)

# Show the plot
fig.show()