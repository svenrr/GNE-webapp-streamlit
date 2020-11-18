"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        st.title("About this project")
        st.markdown(
            """## Idea
This is a project in which we try to differentiate between positive and negative/neutral news from the web automatically. For this we use a variety of machine learning models and dictionary based apporaches to sentiment analysis. Furthermore the goal of this project was to categorize (e.g. business, finance, sports etc.) and summarize news articles. The finished product could either be a website on which users could find only positive news, or a livefeed, where our project could serve as a helpful tool for journalists or similar professions.

## The Developers
This project is developed by Fabian, Sven and Christoph.

## Github
[Good News Everyone Repository](https://github.com/svenrr/good_news_everyone)
""",
            unsafe_allow_html=True,
        )