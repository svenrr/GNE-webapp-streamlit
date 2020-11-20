import logging

import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    """Writes content to the app"""
    st.title('Good News Everyone')
    st.markdown("**The world is better than most people think! Approximately 90% of news on the web are negative and this results in a distorted view of the world.**")
    st.image("./pages/gne-logo.png", width=150)
    #<p align="center"><img src="" alt="logo" width="300"/></p>
    st.write('''This is a project in which we try to differentiate between positive and negative/neutral news from the web automatically. 
    For this we use a variety of machine learning models and dictionary based approaches to sentiment analysis. 
    Furthermore the goal of this project was to categorize (e.g. business, finance, sports etc.) and summarize news articles. 
    On this WebApp you will find an analyser page, on which you can try out our sentiment analysis, categorization and the extractive summary. Furthermore we included a preview of what a live newsfeed could look like in later stages of development.
    Thank you for being interested in our project and now enjoy some good news (hopefully).''')
    
    st.markdown("**General problems about news:**")
    st.markdown("- Opinions are very subjective, whether something is good or bad") 
    st.markdown("- Articles can belong to several categories") 
    st.markdown('- “bad” news are more entertaining')
    
    #st.markdown("![Front Gif](https://motionandmomentum.files.wordpress.com/2017/10/5181a5b8-6e3d-466f-9cea-8f900375fd42-720- 000000640b9c2bac.gif)")
    
if __name__ == "__main__":
    write()
