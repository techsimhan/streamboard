#!/usr/bin/python3.6

import streamlit as st
import wbdata
import pandas as pd 
import pycountry
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
# ----------- Step 1 ------------

def app():
    sources = wbdata.get_source()
    sources_object= {}
    no_of_sources = len(sources)
    for i in range(no_of_sources):
        sources_object[sources[i]["name"]] = sources[i]["id"]
        
    sources_select = st.selectbox("Select your category.", list(sources_object.keys()))

    indicator_list = wbdata.get_indicator(source=sources_object[sources_select])
    indicator_object = {}
    no_of_indicators = len(indicator_list)
    for i in range(no_of_indicators):
        indicator_object[indicator_list[i]["name"]]=indicator_list[i]["id"]
    indicator_select = st.selectbox("Select your indicator.", list(indicator_object.keys()))
    indicator_str = indicator_object[indicator_select]
    #argument_str = "'"+indicator_str+"'" + ':' + "'value'"
    #df = wbdata.get_dataframe({'FP.CPI.TOTL.ZG':'value'},country='all')
    series = wbdata.get_series(indicator_str,country='all')
    series1 = pd.Series(series)
    new_df = series1.unstack()
    test = pd.DataFrame(new_df)
    test1 = test.dropna(axis=1)
    ms_options_countries = st.multiselect("Select the countries you want data",test1.index.tolist())
    ms_option_year = st.multiselect("Select the year you want data",test1.columns.tolist())
    subset = test1.loc[ms_options_countries]
    st.write(subset)
    #fig = px.bar(test1,x=ms_options_countries,y=ms_option_year)
    fig = px.bar(subset,x=subset.index,y='2019')
    st.plotly_chart(fig,use_container_width=True)