#!/usr/bin/python3.6

import streamlit as st
import nsetools as nse
import nsepy
from nsepy import get_history
from nsetools import Nse
import pandas as pd
import numpy as np
from datetime import date
import datetime
import timedelta
from newsapi import NewsApiClient

def app():
    nse = Nse()
    all_stock_codes = nse.get_stock_codes()
    all_stock_codes_values = list(nse.get_stock_codes().values())

    st.title("Stock Screener for NSE")


    stock = st.sidebar.selectbox('select the stock your stock from the list',all_stock_codes_values[1:])
    startDate = st.sidebar.date_input("Select start date",datetime.date(2020, 3, 6))
    endDate = st.sidebar.date_input("Select end date",datetime.date(2020, 7, 6))
    data = get_history(symbol=stock, start=startDate, end=endDate)
    st.write("""### Volume""")
    st.line_chart(data.Volume)
    st.write("""### Closing Price Chart""")
    st.line_chart(data.Close)
    st.write("""### Opening Price Chart""")
    st.line_chart(data.Open)
    st.write("""### High Price Chart""")
    st.bar_chart(data.High)
    st.write("""### Low Price Chart""")
    st.bar_chart(data.Low)
    st.write("""### Opening/Closing Price Chart""")

    reqKey = [key  for (key, value) in all_stock_codes.items() if value == stock]

    quote_stock = nse.get_quote(reqKey[0])

    df=pd.DataFrame(quote_stock.items(),columns=["name","value"])

    st.write(df)


                
                














                    











