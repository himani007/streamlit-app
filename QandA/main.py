import streamlit as st
import pandas as pd

st.write("Here's a dataframe!")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

st.caption('Document Q and A with AI')
st.title('Live demo for using AI and embeddings to answer document based questions with AI.')

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')

a = st.checkbox("Added Minimum 100 words?")



if a==True:
    st.button("Embed Input Doc")

if st.button('Embed Input Doc'):
    
    lent = len(txt)
    st.write(lent)
   
    