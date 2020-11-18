import logging

import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    """Writes content to the app"""
    st.title('Good News Everyone')
    st.write("This is a project in which we try to differentiate between positive and negative/neutral news from the web automatically. For this we use a variety of machine learning models and dictionary based apporaches to sentiment analysis. Furthermore the goal of this project was to categorize (e.g. business, finance, sports etc.) and summarize news articles. The finished product could either be a website on which users could find only positive news, or a livefeed, where our project could serve as a helpful tool for journalists or similar professions.")
    #st.markdown("![Front Gif](https://motionandmomentum.files.wordpress.com/2017/10/5181a5b8-6e3d-466f-9cea-8f900375fd42-720- 000000640b9c2bac.gif)")
    

if __name__ == "__main__":
    write()
