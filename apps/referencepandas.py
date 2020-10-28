#!/usr/bin/python3.6
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

@st.cache #caching for big files
def college_ranking():
    df_collegeranking = pd.read_csv('/home/adminstrator/python_automation/multi_app/apps/National Universities Rankings.csv',encoding='ISO-8859-1')
    #df_collegeranking = pd.read_csv('https://query.data.world/s/42og2ozlow23eiqaidzwsrcwgoyj2t',encoding='ISO-8859-1')
    return df_collegeranking


def app():
    st.header('Pandas for school drop outs')
    st.markdown('---')
    st.markdown("This is a dataframe")
    df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
    st.write(df.head())
    df1 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
    st.write(df1.head())
    df2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],'Sue': ['Pretty good.', 'Bland.']},index=['Product A', 'Product B'])
    st.write(df2.head())
    st.markdown('---')
    st.code('''
    df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
    st.write(df.head())
    df1 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
    st.write(df1.head())
    df2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],'Sue': ['Pretty good.', 'Bland.']},index=['Product A', 'Product B'])
    st.write(df2.head()) ''',language = 'python')
    st.markdown('---')
    st.markdown("This is a Series")
    series1 = pd.Series([1, 2, 3, 4, 5])
    st.write(series1.head())
    series2 = pd.Series([30, 35, 40],index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
    st.write(series2.head())
    st.markdown('---')
    st.code(''' series1 = pd.Series([1, 2, 3, 4, 5])
    st.write(series1.head())
    series2 = pd.Series([30, 35, 40],index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
    st.write(series2.head())''',language='Python')
    st.markdown('---')
    df_colrank = college_ranking() #college Ranking csv use encoding in encoding='ISO-8859-1
    st.write(df_colrank)
    college_list = st.selectbox("Select College", df_colrank["Name"])
    st.markdown('---')
    st.subheader('To print the data frame and creating a indexed select menu')
    st.code('''
    df_colrank = college_ranking() #college Ranking csv use encoding in encoding='ISO-8859-1
    st.write(df_colrank)
    college_list = st.selectbox("Select College", df_colrank["Name"])''',language='Python')
    st.markdown('---')
    st.subheader('function call where the reading of data frame happens & caching incase url csv')
    st.code(''' 
    @st.cache #caching for big files
    def college_ranking():
    #df_collegeranking = pd.read_csv('/home/adminstrator/python_automation/multi_app/apps/National Universities Rankings.csv',encoding='ISO-8859-1')
    df_collegeranking = pd.read_csv('https://query.data.world/s/42og2ozlow23eiqaidzwsrcwgoyj2t',encoding='ISO-8859-1')
    return df_collegeranking ''',language='Python')
    st.markdown('---')
    description = df_colrank.loc[(df_colrank["Name"] == college_list), 'Description'].iloc[0]
    rank = df_colrank.loc[(df_colrank["Name"] == college_list), 'Rank'].iloc[0]
    fees = df_colrank.loc[(df_colrank["Name"] == college_list), 'Tuition and fees'].iloc[0]
    st.markdown(f"<div style=' background-color: YellowGreen; color: Black;font-size: 20px;font-weight: bold;'>Rank of {college_list} :{rank}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style=' background-color: Turquoise; color: Black;font-size: 20px;font-weight: bold;'>Tuition Fees is  {fees}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style=' background-color: IndianRed; color: Black;font-size: 20px;font-weight: bold;'>{description}</div>", unsafe_allow_html=True)
    st.markdown('---')
    st.subheader('To get the values of Description,Rank and Tuition Fees using the unique id college_list & printing with HTML')
    st.code ('''
    description = df_colrank.loc[(df_colrank["Name"] == college_list), 'Description'].iloc[0]
    rank = df_colrank.loc[(df_colrank["Name"] == college_list), 'Rank'].iloc[0]
    fees = df_colrank.loc[(df_colrank["Name"] == college_list), 'Tuition and fees'].iloc[0]
    st.markdown(f"<div style=' background-color: YellowGreen; color: Black;font-size: 20px;font-weight: bold;'>Rank of {college_list} :{rank}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style=' background-color: Turquoise; color: Black;font-size: 20px;font-weight: bold;'>Tuition Fees is  {fees}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style=' background-color: IndianRed; color: Black;font-size: 20px;font-weight: bold;'>{description}</div>", unsafe_allow_html=True)''',language='Python')
    st.markdown('---')
    st.subheader('Multiselect Menu from Dataframe Example')
    app_cols = ["Name","Rank","Tuition and fees","Undergrad Enrollment"]
    ms_options = st.multiselect("Select the columns you want to view",df_colrank.columns.tolist(),default=app_cols)
    st.write(df_colrank[ms_options])
    st.markdown('---')
    st.subheader('Multiselect menu code with data frame display for menu filters')
    st.code('''
    app_cols = ["Name","Rank","Tuition and fees","Undergrad Enrollment"]
    ms_options = st.multiselect("Select the columns you want to view",df_colrank.columns.tolist(),default=app_cols)
    st.write(df_colrank[ms_options])''',language = 'Python')
    st.markdown('---')
    st.subheader('Series Examples')# Defining a series object
    srs = pd.Series([1,2,3,4,5])
    # printing series values
    st.write("The Series values are:")
    st.write(srs.values)
    # # printing series indexes
    st.write("The Index values are:")
    st.write(srs.index.values)
    st.markdown('---')
    # Defining a series object
    srs = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2], index = ['China', 'India', 'USA', 'Brazil', 'Pakistan'])
    # Set Series name
    srs.name = "Growth Rate"
    # Set index name
    srs.index.name = "Country"
    # printing series values
    st.write("The Indexed Series values are:")
    st.write(srs)
    st.markdown('---')
    st.subheader("converting a series to BarChart")
    st.bar_chart(srs)
    st.markdown('---')
    st.subheader('Conveting a dataframe columns  into a barchart')
    df1_colrank = pd.read_csv('/home/adminstrator/python_automation/multi_app/apps/National Universities Rankings.csv',encoding='ISO-8859-1',dtype={'Tuition and fees':str,'Name':str})
    df1_colrank['Tuition and fees'].apply(type).value_counts()
    df1_colrank['Tuition and fees'] = df1_colrank['Tuition and fees'].str.replace(',','').str.replace('$','').astype('float')
    fee_fig = px.bar(df1_colrank, x='Name', y='Tuition and fees')
    st.plotly_chart(fee_fig,use_container_width=True)
    st.markdown('---')
    st.code('''df1_colrank = pd.read_csv('/home/adminstrator/python_automation/multi_app/apps/National Universities Rankings.csv',encoding='ISO-8859-1',dtype={'Tuition and fees':str,'Name':str})
    df1_colrank['Tuition and fees'].apply(type).value_counts()
    df1_colrank['Tuition and fees'] = df1_colrank['Tuition and fees'].str.replace(',','').str.replace('$','').astype('float')
    fig = px.bar(df1_colrank, x='Name', y='Tuition and fees')
    st.plotly_chart(fig,use_container_width=True)''')
    st.markdown('---')
    rank_fig = px.bar(df1_colrank, x='Name', y='Rank')
    st.plotly_chart(rank_fig,use_container_width=True)
    st.markdown('---')

