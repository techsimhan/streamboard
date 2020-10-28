#!/usr/bin/python3.6

import streamlit as st
import pandas as pd 
import wbdata
import plotly.express as px
import pycountry
from streamlit_folium import folium_static
import folium

def app():
    st.title("Here is your much awaited WorldBank Dashboard")
    wb_country = wbdata.get_country()
    wb_count = len(wb_country)
    wb_country_dic ={}
    for i in range(wb_count):
        if wb_country[i]["capitalCity"]!= "":
            wb_country_dic[wb_country[i]["name"]]=wb_country[i]["id"]
    wb_country_select = st.sidebar.selectbox("select World Bank Country",list(wb_country_dic.keys()))

        
    sources = wbdata.get_source()
    sources_object= {}
    no_of_sources = len(sources)
    for i in range(no_of_sources):
        sources_object[sources[i]["name"]] = sources[i]["id"]
        
    sources_select = st.sidebar.selectbox("Select your category.", list(sources_object.keys()))

    indicator_list = wbdata.get_indicator(source=sources_object[sources_select])
    indicator_object = {}
    no_of_indicators = len(indicator_list)
    for i in range(no_of_indicators):
        indicator_object[indicator_list[i]["name"]]=indicator_list[i]["id"]
    indicator_select = st.sidebar.selectbox("Select your indicator.", list(indicator_object.keys()))
    country_id = wbdata.search_countries(wb_country_select)
    country_map = folium.Map(location=[country_id[0]["latitude"],country_id[0]["longitude"]],zoom_start=3,zoom_control=True,width='70%',height='85%')
    tooltip = "Liberty Bell"
    folium.Marker(
            [country_id[0]["latitude"],country_id[0]["longitude"]], popup="Liberty Bell", tooltip=tooltip
        ).add_to(country_map)
    folium_static(country_map)
        #data_indicator = wbdata.get_data(indicator_object[indicator_select],country=wb_country_dic[wb_country_select])
    indicator_str = indicator_object[indicator_select]
    country_str = wb_country_dic[wb_country_select]
    st.write(indicator_select)
    st.write(country_str)
    data_indicator = wbdata.get_data(indicator_str,country=country_str)
    df_indicator = pd.DataFrame.from_dict(data_indicator)
    rank_fig = px.bar(df_indicator, x='date', y='value')
    st.plotly_chart(rank_fig,use_container_width=True,sharing ="streamlit")
    world_countries_data = pd.read_csv('/home/adminstrator/python_automation/multi_app/apps/2015.csv',encoding='ISO-8859-1')
    multiple_select_data = pd.read_csv('/home/adminstrator/python_automation/multi_app/apps/2015.csv',encoding='ISO-8859-1')
    multiple_select_data.drop('Country',axis=1,inplace=True)
    multiple_select_data.drop('Region',axis=1,inplace=True)
    ms_option = st.multiselect("Select 2015 Data Set",multiple_select_data.columns.tolist())
    for i in range(len(ms_option)):
        fig_world = px.sunburst(world_countries_data,path=["Region","Country"],values=ms_option[i],width=750, height=750,title=ms_option[i])
        st.write(fig_world)
    #all_data = wbdata.get_dataframe(indicator_object[indicator_select],country=country_object[country_select])
    #pycountry country select bar
        #country_object = {}
        #no_of_country = len(pycountry.countries)
        #for i in range(no_of_country):
            #country_string = list(pycountry.countries)[i]
            #country_object[country_string.name]=country_string.alpha_2 #pushing keys and values to dictionary
        #country_select = st.selectbox("Select your country.", list(country_object.keys()))"""
