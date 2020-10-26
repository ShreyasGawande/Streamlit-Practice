import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price app
""")
tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf=tickerData.history(period='2d',start='2020-1-31',end='2020-5-31')
#Open High Low Close Volume Dividends Stock Splits
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume price
""")
st.line_chart(tickerDf.Volume)
