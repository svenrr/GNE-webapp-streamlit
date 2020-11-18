"""Main module for the streamlit app"""
import streamlit as st
import awesome_streamlit as ast


import pages.home
import pages.analysis
import pages.eda
import pages.about
import pages.livefeed

ast.core.services.other.set_logging_format()

PAGES = {
    "Home": pages.home,
    "Article Analysis" : pages.analysis,
    "Data Analysis" : pages.eda,
    "Newsfeed" : pages.livefeed,
    "About": pages.about,
    
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()