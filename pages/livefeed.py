import logging
import streamlit as st
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
import pandas as pd
from Functions.sum_functions import * 

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    
    st.title('Newsfeed Preview')
    
    st.sidebar.title('Information')
    st.sidebar.info('In the future we could include more filters (e.g. date of publishing)')
    sentiment_choice = st.sidebar.multiselect('Select Sentiment', ['good', 'neutral/bad'], default=['good'])
    category_choice = st.sidebar.multiselect('Select Category', ['entertainment', 'financial', 'politics', 'sports', 'technology', 'travel', 'world'])

    
    for idx, sentiment in enumerate(sentiment_choice):
        if sentiment == 'good':
            sentiment_choice[idx] = 1
        if sentiment== 'neutral/bad':
            sentiment_choice[idx] = 0

    
    col_input, col_control= st.beta_columns((2,4)) # define 2 columns to control size of input box
    with col_input:
        num_articles = st.number_input('Enter the desired number of articles you want to see', min_value=1, value=10)
        
    
    if st.button('Generate feed'):
        df = pd.read_csv('data/news_actual_preprocessed.csv')
        
        if not sentiment_choice:
            sentiment_choice = [0,1]
        
        if not category_choice:
            category_choice = ['entertainment', 'financial', 'politics', 'sports', 'technology', 'travel', 'world']
        
        
        df = df.query(f'sentiment == {sentiment_choice}')
        df = df.query(f'category == {category_choice}')
        
        if df.shape[0] <= num_articles:
            num_articles = df.shape[0]
    
        col1, col2, col3= st.beta_columns((3,0.2,3)) # generate 3 columns where the middle one functions as a seperator
        with col1:
            for idx in range(int(num_articles/2)): # display first column
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
            for idx in range(int(num_articles/2), num_articles): # display second column
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
