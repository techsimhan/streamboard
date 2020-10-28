#!/usr/bin/python3.6
import streamlit as st
from newsapi import NewsApiClient
import pycountry
import random

css_colors = ["AliceBlue",
  "AntiqueWhite",
  "Aqua",
  "Aquamarine",
  "Azure",
  "Beige",
  "Bisque",
  "Black",
  "BlanchedAlmond",
  "Blue",
  "BlueViolet",
  "Brown",
  "BurlyWood",
  "CadetBlue",
  "Chartreuse",
  "Chocolate",
  "Coral",
  "CornflowerBlue",
  "Cornsilk",
  "Crimson",
  "Cyan",
  "DarkBlue",
  "DarkCyan",
  "DarkGoldenRod",
  "DarkGray",
  "DarkGrey",
  "DarkGreen",
  "DarkKhaki",
  "DarkMagenta",
  "DarkOliveGreen",
  "Darkorange",
  "DarkOrchid",
  "DarkRed",
  "DarkSalmon",
  "DarkSeaGreen",
  "DarkSlateBlue",
  "DarkSlateGray",
  "DarkSlateGrey",
  "DarkTurquoise",
  "DarkViolet",
  "DeepPink",
  "DeepSkyBlue",
  "DimGray",
  "DimGrey",
  "DodgerBlue",
  "FireBrick",
  "FloralWhite",
  "ForestGreen",
  "Fuchsia",
  "Gainsboro",
  "GhostWhite",
  "Gold",
  "GoldenRod",
  "Gray",
  "Grey",
  "Green",
  "GreenYellow",
  "HoneyDew",
  "HotPink",
  "IndianRed",
  "Indigo",
  "Ivory",
  "Khaki",
  "Lavender",
  "LavenderBlush",
  "LawnGreen",
  "LemonChiffon",
  "LightBlue",
  "LightCoral",
  "LightCyan",
  "LightGoldenRodYellow",
  "LightGray",
  "LightGrey",
  "LightGreen",
  "LightPink",
  "LightSalmon",
  "LightSeaGreen",
  "LightSkyBlue",
  "LightSlateGray",
  "LightSlateGrey",
  "LightSteelBlue",
  "LightYellow",
  "Lime",
  "LimeGreen",
  "Linen",
  "Magenta",
  "Maroon",
  "MediumAquaMarine",
  "MediumBlue",
  "MediumOrchid",
  "MediumPurple",
  "MediumSeaGreen",
  "MediumSlateBlue",
  "MediumSpringGreen",
  "MediumTurquoise",
  "MediumVioletRed",
  "MidnightBlue",
  "MintCream",
  "MistyRose",
  "Moccasin",
  "NavajoWhite",
  "Navy",
  "OldLace",
  "Olive",
  "OliveDrab",
  "Orange",
  "OrangeRed",
  "Orchid",
  "PaleGoldenRod",
  "PaleGreen",
  "PaleTurquoise",
  "PaleVioletRed",
  "PapayaWhip",
  "PeachPuff",
  "Peru",
  "Pink",
  "Plum",
  "PowderBlue",
  "Purple",
  "Red",
  "RosyBrown",
  "RoyalBlue",
  "SaddleBrown",
  "Salmon",
  "SandyBrown",
  "SeaGreen",
  "SeaShell",
  "Sienna",
  "Silver",
  "SkyBlue",
  "SlateBlue",
  "SlateGray",
  "SlateGrey",
  "Snow",
  "SpringGreen",
  "SteelBlue",
  "Tan",
  "Teal",
  "Thistle",
  "Tomato",
  "Turquoise",
  "Violet",
  "Wheat",
  "White",
  "WhiteSmoke",
  "Yellow",
  "YellowGreen",
]

def app():

    st.title("Get the news by Country & Category")
    newsapi = NewsApiClient(api_key='acb4c1098cb446ab802cce2402c69f3c')
    input_countries = ('Argentina','Australia','Austria','Belgium','Brazil','Bulgaria','Canada','China','Colombia','Cuba','Czech Republic','Egypt','France','Germany','Greece','Hong Kong','Hungary','India','Indonesia','Ireland','Israel','Italy','Japan','Latvia','Lithuania','Malaysia','Mexico','Morocco','Netherlands','New Zealand','Nigeria','Norway','Philippines','Poland','Portugal','Romania','Russia','Saudi Arabia','Serbia','Singapore','Slovakia','Slovenia','South Africa','South Korea','Sweden','Switzerland','Taiwan','Thailand','Turkey','UAE','Ukraine','United Kingdom','United States','Venuzuela','Argentina')
    country_options = list(range(len(input_countries)))
    country_name = st.selectbox("countries",country_options, format_func=lambda x: input_countries[x])
    input_category = ('business','entertainment','general','health','science','sports','technology')
    category_option = list(range(len(input_category)))
    category_index = st.selectbox("category",category_option, format_func=lambda y: input_category[y])
    input_category[category_index]
    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2
    '''codes = [countries.get(country, 'Unknown code') for country in input_countries]'''
    country_code = ''
    country1 = input_countries[country_name]
    country_code = [countries.get(country1,'Unknown code')]
    top_headlines = newsapi.get_top_headlines(category=input_category[category_index],language='en',country=country_code[0].lower())
    if top_headlines.get('totalResults')!=0:
        st.subheader('Your Top Headlines For Now')
        for i in top_headlines['articles']:
            for k,v in i.items():
                if k == 'title':
                    st.markdown(f"<div class = 'center' style=' background-color: {random.choice(css_colors)}; color: black;font-size: 20px;font-weight: bold;'>{v}</div>", unsafe_allow_html=True)
                if k=='urlToImage':
                    st.markdown(f"<img class = 'card' src='{v}'  alt='Image not Accessible' width='500' height='600'>",unsafe_allow_html=True)
                    st.markdown("---")
                if k== 'url':
                    st.write(v)

















                    











