import logging
import streamlit as st
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
import pandas as pd
from Functions.sum_functions import * 

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    
    num_articles = 1
    st.title('Newsfeed Preview')
    
    st.sidebar.title('Information')
    st.sidebar.info('In the future we would like to include filters for the feed. For example to only show one sentiment, certain categories or publishers etc.')
    
    col_input, col_control= st.beta_columns((1,5))
    with col_input:
        num_articles = st.number_input('Enter the desired number of articles you want to see (1 to 100)', min_value=1, max_value = 100, value=10)
        
    
    if st.button('Generate feed'):
        df = pd.read_csv('data/news_actual_preprocessed.csv')
        
    
        col1, col2, col3= st.beta_columns((3,0.2,3))
        with col1:
            for idx in range(int(num_articles/2)):
                title_text = f'**[{df.iloc[idx].title}]({df.iloc[idx].url})**'
                st.markdown(title_text)
                if df.iloc[idx].sentiment == 0:
                    st.write('Sentiment: neutral/negative')
                else:
                    st.write('Sentiment: positive')
                st.write('Category:', df.iloc[idx].category)
                with st.beta_expander('Summary'):
                    summary = get_summary(df.iloc[idx].text)
                    for phrase in range(len(summary)): 
                        st.write("- ",summary[phrase],"\n")
            
        with col3:
            for idx in range(int(num_articles/2), num_articles):
                title_text = f'**[{df.iloc[idx].title}]({df.iloc[idx].url})**'
                st.markdown(title_text)
                if df.iloc[idx].sentiment == 0:
                    st.write('Sentiment: neutral/negative')
                else:
                    st.write('Sentiment: positive')
                st.write('Category:', df.iloc[idx].category)
                with st.beta_expander('Summary'):
                    summary = get_summary(df.iloc[idx].text)
                    for phrase in range(len(summary)): 
                        st.write("- ",summary[phrase],"\n")
        

if __name__ == "__main__":
    write()