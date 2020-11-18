import logging

import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    """Writes content to the app"""
    st.title('Livefeed')
    st.selectbox('Select sources', ['All', 'bbc', 'cnn'])
    st.multiselect('Select categories', ['Finance', 'Politics', 'Sports'])

    
    
    
    
    
    
    
    
if __name__ == "__main__":
    write()