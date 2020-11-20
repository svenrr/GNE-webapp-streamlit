import logging
import pandas as pd
import streamlit as st
import awesome_streamlit as ast
import matplotlib.pyplot as plt
from awesome_streamlit.core.services import resources
from Functions.plots_fabi import *
import numpy as np
import plotly.express as px
from datetime import datetime



logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    
    st.title('Data Analysis')
    st.write("This is a preview of what kind of data analysis we think could be useful to perform with the newsfeed data. Please be reminded that we don't have a lot of data at this point. So some of the graphs don't make a lot of sense yet.")
    st.text("")
    st.text("")
    
    
    ######Preprocessing
    #################################################################
    df = pd.read_csv('data/news_actual_preprocessed.csv')
    df.sentiment = ['Good' if val == 1 else 'Neutral/Bad' for val in df.sentiment]
    conv = {
    'BBC': '%Y-%m-%dT%H:%M:%S',
    'CNN': '%Y-%m-%dT%H:%M:%SZ'
    }

    df.date_published = [datetime.strptime(time, conv[pub]) for time, pub in zip(df.date_published.values, df.publisher.values)]
    
    def to_datetime(time):
        return datetime.utcfromtimestamp(time.astype(int) * 1e-9)

    df['day_published'] = [to_datetime(time).day for time in df.date_published.values]
    df['weekday_published'] = [to_datetime(time).weekday() for time in df.date_published.values]
    df['month_published'] = [to_datetime(time).month for time in df.date_published.values]
    df['year_published'] = [to_datetime(time).year for time in df.date_published.values]

    # 4 Articles from 2019, 9 Articles from 2020, Remove them
    df = df[df.year_published > 2019]

    # Remove Articles from before November
    df = df[df.month_published > 10]

    # Remove Articles from before November 10
    limit = datetime.strptime('2020-11-10', '%Y-%m-%d')
    df = df[[(pub-limit).days > 0 for pub in df.date_published]]
    
    ###################################################################
    
    
    # Pie chart for Sentiment distribution
    st.write('**Distribution of good and neutral/bad articles in the newsfeed dataset**')
    
    col1, col2, col3= st.beta_columns((3,0.2,3))
    
    with col1:
        fig_pie, ax = plt.subplots(figsize=(4,4))
        plt.pie(df.sentiment.value_counts().values, explode=(0,0.2), autopct='%1.1f%%', labels=df.sentiment.value_counts().keys(), startangle=30, labeldistance=1.2, shadow=False)
        st.pyplot(fig_pie)
    
    # Description
    with col3:
        st.write(f' As we already explained on the Frontpage, there exists more neutral or negative news than bad. This is the percentage we get with our current model for sentiment analysis, which is manipulable through a given threshold. This chart is based on {df.shape[0]} articles, which were scraped from BBC and CNN.')
    
    ####################################################################
    
    # Bar chart for number of articles posted on each weekday
    st.write('**Mean number of articles posted on each weekday**')
    l = []
    for date in df.date_published:
        l.append((date.weekday(), date.day))
    u = np.unique(l, axis=0)
    weight = pd.DataFrame({'day': [i[0] for i in u]}).day.value_counts(sort=False)
    x = np.sort(np.unique(df.weekday_published.unique()))
    published = df.groupby('sentiment').weekday_published.value_counts()
    y = {}
    for sent in df.sentiment.unique():
        keys = list(published[sent].keys())
        vals = list(published[sent].values)
        # Insert missing values
        if len(keys) < len(x):
            for x_value in x:
                if x_value not in keys:
                    keys.append(x_value)
                    vals.append(0)
        _, vals = zip(*sorted(zip(keys, vals)))
        # Get mean
        vals = [v/w for v, w in zip(vals, weight)]
        y[sent] = vals
    # Rename x
    x = [{0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat',  6: 'Sun'}[x_] for x_ in x]
    fig_bar_num = bar_adjacent_labels(x, y, ylabel='Number of articles')
    st.pyplot(fig_bar_num)

    ####################################################################
    
    # Distribution of articles between categories
    st.write('**Distribution of articles between categories**')
    x, y = zip(*sorted(zip(df.category.value_counts().keys(), df.category.value_counts().values)))
    fig_bar = plt.figure(figsize=(10,6))
    plt.bar(x, y, edgecolor='black')
    plt.ylabel('Number of articles');
    st.pyplot(fig_bar)
    
    ####################################################################
    
    # Distribution of good and bad articles between categories
    st.write('**Distribution of good and bad articles between categories**')
    
    # Data
    x = np.sort(np.unique(df.category.unique()))
    published = df.groupby('sentiment').category.value_counts()
    y = {}
    for sent in df.sentiment.unique():
        keys = list(published[sent].keys())
        vals = list(published[sent].values)
        # Insert missing values
        if len(keys) < len(x):
            for x_value in x:
                if x_value not in keys:
                    keys.append(x_value)
                    vals.append(0)

        _, vals = zip(*sorted(zip(keys, vals)))
        y[sent] = vals
    
    # Plot
    fig_bar_cat = bar_adjacent_labels(x, y, ylabel='Number of articles')
    st.pyplot(fig_bar_cat)
    
    ####################################################################
    
    # Text length
    st.write('**Distribution of good and bad articles between publishers**')
    # Get textlength and bin text length
    df['text_length'] = [100*int(len(text.split(' '))/100) for text in df.text]
    # Put textlength > 1600 together
    df.text_length = [l if l <= 1600 else 1700 for l in df.text_length]
    x = np.sort(np.unique(df.text_length.unique()))
    published = df.groupby('sentiment').text_length.value_counts()
    y = {}
    for sent in df.sentiment.unique():
        keys = list(published[sent].keys())
        vals = list(published[sent].values)
        # Insert missing values
        if len(keys) < len(x):
            for x_value in x:
                if x_value not in keys:
                    keys.append(x_value)
                    vals.append(0)
    
        _, vals = zip(*sorted(zip(keys, vals)))
        y[sent] = vals
    
    # Rename highest x
    x = [str(x_) for x_ in x]
    x[-1] = '<1600'
    
    fig_bar_text_length = bar_adjacent_labels(x, y, ylabel='Number of articles')
    st.pyplot(fig_bar_text_length)
    
    ####################################################################
    
if __name__ == "__main__":
    write()