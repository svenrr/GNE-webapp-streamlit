import logging
import streamlit as st
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
import praw
import pandas as pd 
from Functions.word_frequency import word_frequency
import base64
import altair as alt
import spacy
from pytrends.request import TrendReq
import time
import datetime

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

#######################################################################################################################################################

# function to download generated dataframes as csv file 
def get_table_download_link(df, filename="filename.csv"):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download={filename}>Download as csv file</a>'
    return href

#######################################################################################################################################################

def write():
    st.write("# Trend topics & content ideas")
    st.write('''In the following, different sources are used to quickly gain an overview of current topics in the world or a specific industry. 
            These insights can also be used by journalists, bloggers, etc. to report on topics that are currently of particular interest and most talked about. 
            Currently, information can be displayed via Google Trends, Twitter and Reddit. Bigger tables can also be downloaded directly as csv files.''')
    
    st.write("----")
    st.write("## Reddit")
    # Load the login credentials and setup the Reddit API
    r_details = pd.read_csv("https://docs.google.com/spreadsheets/d/1WO4GedbP8xiNuLhZc20k51DrCNAmKpL4Uit15pNEqe0/export?gid=0&format=csv")
    r = praw.Reddit(client_id=r_details.client_id[0], client_secret=r_details.client_secret[0], user_agent='Henlo')

    ###########

    # Load the the data of the relevant subreddits about news 
    srds = pd.read_csv("https://github.com/svenrr/good_news_everyone/raw/main/Datasets/dataset_subreddits_for_eda/subreddits.csv",encoding="cp1252")
    with st.beta_expander('Relevant subreddits for any kind of news'): # hide them 
        st.dataframe(srds)

    ##########

    st.write("We take the top 10 subreddits with the most subscribers and search for the top 10 hot topics in there. You can change that if you want.")
    srds_top10 = srds.sort_values(by=" subs",ascending=False)[0:10]
    st.dataframe(srds_top10)

    r_ms = st.multiselect("Select subreddits", [i for i in srds.reddit], default=[i for i in srds_top10.reddit]) # Enable selection of subreddits

    topic_lst = []
    reddit_dict = {"subreddit": [], "title": [], "upvote_ratio": [], "num_comments": []} # Save reddit & submission details 

    # Get the details & information
    for subr in r_ms: # For Subreddit in Subreddit-List 
        for submission in r.subreddit(subr).hot(limit=10): # For Reddit-Post in Subreddit -> Top10 of hot posts 
            topic_lst.append(submission.title)
            reddit_dict["subreddit"].append(subr)
            reddit_dict["title"].append(submission.title)
            reddit_dict["upvote_ratio"].append(submission.upvote_ratio)
            reddit_dict["num_comments"].append(submission.num_comments)
           #reddit_dict["score"].append(submission.score)

    st.write("Number of total submissions: {}".format(len(topic_lst)))

    reddit_df = pd.DataFrame(reddit_dict)

    with st.beta_expander('Show full text'): # Hide the output
        st.table(reddit_dict["title"])

    with st.beta_expander('Show more information & optional download'): # Show additional information like num. of comments
        st.markdown(get_table_download_link(reddit_df, filename="reddit_news.csv"), unsafe_allow_html=True) # Allow/enable download 
        st.dataframe(reddit_df)#.drop(columns="title", axis=0)) 

    #st.write("Number of comments: ", reddit_df[reddit_df["subreddit"] == "WorldNews"].num_comments.sum(axis=0))

    word_frequency(". ".join(topic_lst)) # Function to get top keywords & create a wordcloud

    #######################################################################################################################################################

    st.markdown("### Search posts about a specific keyword")
    r_search_input = st.text_input("Enter a keyword", "bitcoin")
    r_search_sort = st.selectbox("Select sorting option", ["relevance", "hot", "top", "new", "comments"], key="r_search_sort") # search option
    r_search_time = st.selectbox("Select time filter option", ["all", "day", "month", "week", "year"], key="r_search_time") # time option
    r_search_output = st.slider("How many results should be displayed?", min_value=5, max_value=100, value=10, step=5) # slider to select output amount

    reddit_search_dict = {"title": [], "score": [], "url": []} #, "num_comments": [], "upvote_ratio": []} # save the information

    #search_lst = []
    # Iterates through all subreddits to reddit and searches for the occurrence of the keyword
    for submission in r.subreddit("all").search(r_search_input, sort=r_search_sort, time_filter=r_search_time): 
        reddit_search_dict["title"].append(submission.title)
        reddit_search_dict["score"].append(submission.score)
        reddit_search_dict["url"].append("www.reddit.com" + submission.permalink)
        #search_lst.append(submission.title)
        #add upvote_ratio or score
        #add id/url to find post

    r_search_df = pd.DataFrame(reddit_search_dict) # save the results as dataframe
    r_search_df.drop(columns="url", axis=1, inplace=True) # drop url column
    #st.write(search_lst[0:r_search_output])
    st.table(r_search_df.iloc[0:r_search_output]) # Output as static table 
    st.markdown(get_table_download_link(r_search_df.iloc[0:r_search_output], filename="reddit_search.csv"), unsafe_allow_html=True) # enable download

    #######################################################################################################################################################
    st.write("---")
    st.markdown("## Google")
    pytrend = TrendReq() # google setup

    st.write("## Related queries")

    search_topic = st.text_input("Enter a keyword or topic...","Data Science",key="gtrend") # keyword to look for 

    sb_torr = st.selectbox("Select one option", ["top", "rising"], key="sb_torr") # option: top or rising?

    # setup
    pytrend.build_payload(kw_list=[search_topic])
    related_queries = pytrend.related_queries()
    rq_df = pd.DataFrame(related_queries.get(search_topic).get(sb_torr)) # save the results as dataframe

    st.dataframe(rq_df) # display the results 

    #######
    st.write("---")
    st.markdown("### Interest over time (US)")

    rd_tf = st.radio("Select google property (default = web searches)", ["","news", "youtube"]) # search option 
    sb_tf = st.selectbox("Select a timeframe", ["today 5-y", "today 3-y", "today 12-m", "today 3-m", "today 1-m"] , key="sb_tf") # time filter/periode
    iot_kws = st.text_input("Enter keywords and use comma as delimiter","python, java, html, javascript, sql", key="giot") # keywords to compare 
    keywords = list(iot_kws.split(",")) # preparation for input 
    interest_over_time = pytrend.build_payload(keywords, timeframe=sb_tf, geo="US", gprop=rd_tf)
    iot = pd.DataFrame(pytrend.interest_over_time()) # save as dataframe
    iot.drop("isPartial",axis=1, inplace=True) # drop unnecessary column 

    st.line_chart(iot) # show the results as line plot

    with st.beta_expander('Show more details'): # Hide the output / dataframe which was used to create the lineplot
        st.dataframe(iot)
        st.markdown(get_table_download_link(iot, filename="google_interest_over_time.csv"), unsafe_allow_html=True) # enable download 
        st.markdown("**Interest by region**")
        ibr = pytrend.interest_by_region(resolution='REGION', inc_low_vol=True, inc_geo_code=False)
        st.dataframe(ibr)
    
if __name__ == "__main__":
    write()
