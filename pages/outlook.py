import logging
import streamlit as st
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    st.markdown("# Outlook")
    st.write('''On this page we will discuss problems that we have noticed during our work and what would be possible solutions. 
    Furthermore, possible and potential features are shown.''')
    st.markdown("----")
    #st.markdown("**Problems & Improvements:**")  
    with st.beta_expander("Problems & Improvements"):
            st.write("""
        * Dataset
          * Properly labeled
          * Improved cleaning
          * More articles (balanced publishers, categories and release dates)
          * Category dataset only includes articles from 2015
        * Web-Scraping limited to 2 sources at this point in time (bbc & cnn)
          * NewsAPI.org could be a solution (high monthly costs)
        * Newsfeed is not actually a live feed (we scrape data, then process and implement it into the app as a preview)
        """)
    st.write(" ")
    #st.markdown("**Future Work & Ideas:**") 
    with st.beta_expander("Future Work & Ideas"):
        st.markdown("- API that forwards all good news and makes it available to other publishers who also want to display only good news")
        st.markdown("- Twitter bot that only tweets good news") 
        st.markdown("- Social Media Sentiment Analysis for comments (i.e. reddit or twitter) in posts about news")
        st.markdown("- Optimization of the website and possibly deploy via FastAPI or Flask to have more options/functionality") 


    
if __name__ == "__main__":
    write()
