#!/usr/bin/python3.6

import streamlit as st
from multiapp import MultiApp
from apps import referencepandas,stocks,news,worldbank_single,covid_spread,gapminder_choropleth # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("News",news.app)
app.add_app("Stocks",stocks.app)
app.add_app("COVID19-Worldspread",covid_spread.app)
app.add_app("World Bank Data",worldbank_single.app)
app.add_app("Gapminder Data",gapminder_choropleth.app)
app.add_app("pandas",referencepandas.app)

# The main app
app.run()
