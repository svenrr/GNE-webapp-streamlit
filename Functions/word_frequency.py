##### Imports & Setup #####

import spacy
from collections import Counter
from string import punctuation
import math
import en_core_web_sm
import streamlit as st
import pandas as pd 
import altair as alt
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

nlp = en_core_web_sm.load()

##### Function #####

def word_frequency(article_text):
    '''Input: An article text
    Output: A summarization'''
    from spacy.lang.en.stop_words import STOP_WORDS # Get english stopwords from spaCy
    stopwords = list(STOP_WORDS)
    
    doc = nlp(article_text.lower()) 
    
    # Count the word frequency and save it in a dictionary 
    word_freqs = {}
    for word in doc:
        if (word.text not in stopwords and word.text not in punctuation and word.text not in '“”‘’'):
            if word.text not in word_freqs.keys():
                word_freqs[word.text] = 1
            else:
                word_freqs[word.text] += 1
    
    # Sort the dictionary in descending order starting from the most common word
    sort_orders = sorted(word_freqs.items(), key=lambda x: x[1], reverse=True)
    st.write("**Words that appear more than three times:**")

    # Save the results in a dataframe but only the words that occur more than 2 times
    wf_dic = dict()
    for i in sort_orders: 
        if i[1] > 3:
            wf_dic.update({i[0] : i[1]})
    
    wf_df = pd.DataFrame(wf_dic, index=["Word Frequencies"])
    st.dataframe(wf_df) # Display the dataframe on the webapp 
    
    # Create and generate a word cloud image:
    wc_txt = ""
    for k,v in wf_df.items(): 
      tmp = k + " " 
      wc_txt += (tmp*int(v))
        
    wordcloud = WordCloud(background_color='white').generate(wc_txt)

    # Display the generated image/wordcloud:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot() # Display the wordlcoud on the webapp 
