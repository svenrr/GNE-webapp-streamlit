"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
  
    with st.spinner("Loading About ..."):
        st.title("About us")
        st.markdown("![Good News](https://motionandmomentum.files.wordpress.com/2017/10/5181a5b8-6e3d-466f-9cea-8f900375fd42-720-000000640b9c2bac.gif)")
        st.markdown(
            """## Project
This is our one month final project from the Data Science Bootcamp of neuefische. This was a group work, which we approached in a team of three people. If you have any questions or similar, feel free to contact us directly via LinkedIn. You can also find more information about us on the [talent website](https://talents.neuefische.de/?role=Data%20Scientist&alumniLocation=K%C3%B6ln) of neuefische.  

## The Developers
This project is developed by [Fabian März](https://www.linkedin.com/in/fabian-m%C3%A4rz-3913981b3/), [Sven Rutsch](https://www.linkedin.com/in/sven-rutsch-b9728612b/) and [Christoph Blickle](https://www.linkedin.com/in/christoph-blickle-4064ab1ba).

## Github
[Good News Everyone Repository](https://github.com/svenrr/good_news_everyone)
""",
            unsafe_allow_html=True,
        )
