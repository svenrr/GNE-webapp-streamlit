import logging

import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    """Writes content to the app"""
    st.title('Good News Everyone')
    #st.markdown("![Front Gif](https://motionandmomentum.files.wordpress.com/2017/10/5181a5b8-6e3d-466f-9cea-8f900375fd42-720- 000000640b9c2bac.gif)")
    

if __name__ == "__main__":
    write()