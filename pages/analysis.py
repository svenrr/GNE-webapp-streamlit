import logging
import streamlit as st
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

# Modules for this site
import numpy as np
import pandas as pd
from Functions.Preprocessor import Preprocessor
from Functions.sentiment import analyse
from Functions.categorizer import Categorizer
from Functions.sum_functions import * 

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

def write():
    # Write content to the page
    
    # Display title and text
    st.title('Analysis')
    st.write('On this page you can try out our analyser algorithm. Copy and past a article of your chosing into the space below and see what happens.')
    
    # Box for User input
    user_input = st.text_area('Your text:', 
    '''US-based researchers have developed a process for recycling lithium-ion batteries that consumes around 80 to 90 per cent less energy than current methods, and cuts greenhouse gas emissions by about 75 per cent. Lithium-ion battery production has been booming in recent years due to their broad use in consumer technology like smartphones and laptops, in addition to being a key part of the rapidly growing electric vehicle market. The new process developed by a team at the University of California San Diego is designed to restore spent cathodes to mint condition. It works particularly well on cathodes made from lithium iron phosphate, or LFP. Batteries made with LFP cathodes are less costly than other lithium-ion batteries because they don’t use expensive metals like cobalt or nickel. LFP batteries also have longer lifetimes, are safer and are already widely used in power tools, electric buses and energy grids. They are also the battery of choice for Tesla’s Model 3. “Given these advantages, LFP batteries will have a competitive edge over other lithium-ion batteries in the market,” said Zheng Chen, a professor of nanoengineering at UC San Diego.
The new process should help to lower the high costs of recycling as it can be undertaken at low temperatures (60 to 80 C) and ambient pressure, making it less power-hungry than other methods. Also, the chemicals it uses—lithium salt, nitrogen, water and citric acid—are inexpensive and benign. “The whole regeneration process works at very safe conditions, so we don’t need any special safety precautions or special equipment. That’s why we can make this so low cost for recycling batteries,” said first author Panpan Xu. The researchers first cycled commercial LFP cells until they had lost half their energy storage capacity. They took the cells apart, collected the cathode powders, and soaked them in a solution containing lithium salt and citric acid. Then they washed the solution with water, dried the powders and heated them. The researchers made new cathodes from the powders and tested them in both coin cells and pouch cells. Their electrochemical performance, chemical make-up and structure were all fully restored to their original states. As the battery cycles, the cathode undergoes two main structural changes that are responsible for its decline in performance. The first is the loss of lithium ions, which creates empty sites called vacancies in the cathode structure. The other occurs when iron and lithium ions switch spots in the crystal structure. When this happens, they cannot easily switch back, so lithium ions become trapped and can no longer cycle through the battery. The process restores the cathode’s structure by replenishing lithium ions and making it easy for iron and lithium ions to switch back to their original spots.
While the overall energy costs of this recycling process are lower, researchers say further studies are needed on the logistics of collecting, transporting and handling large quantities of batteries.''', height=256)
    
    # Create class instance
    text = Preprocessor(user_input)
    
    # Sidebar
    st.sidebar.title('Features')
    st.sidebar.info('You can chose a few more features that will be displayed if you want to')
    show_tokenization = st.sidebar.checkbox("Show Tokenization") # checkboxes for features
    show_readability = st.sidebar.checkbox("Show readability of the article")
    show_word_frequency = st.sidebar.checkbox("Show word frequency")
    show_reading_time = st.sidebar.checkbox("Show reading time")
       
    ### Main Functions ###
    user_input_per = st.slider('Here you can chose by how much percent the article should be reduced for the summary', min_value=0.1, max_value=0.9, value=0.9, step=0.05) # Display slider 
    if st.button('Analyse'):
        
        # Sentiment
        result = analyse(text.transform()) # Predict Sentiment on vectorized data
        st.write('**Sentiment:**', result) 
    
        # Category
        st.write('**Category:**', Categorizer().pred(text.lem_text()).capitalize())
    
        # Summary
        summary = get_summary(user_input, (1-user_input_per)) # Summary length dependend on slider position
        st.write('**Extractive Summary:**')
        st.write(get_tags(user_input))
        
        for i in range(len(summary)): 
            st.write("- ",summary[i],"\n")
    
        # Features
        if show_tokenization:
            st.write('**Tokens:**', text.lem_text())
            
        if show_readability:
            st.write('**Readability:**', readability(user_input))
            
        if show_word_frequency:
            st.write('**Word frequency:**', word_frequency(user_input))
            
        if show_reading_time:
            st.write('**Reading time:**', str(reading_time(user_input)) + ' min')
        
        
        
if __name__ == "__main__":
    write()