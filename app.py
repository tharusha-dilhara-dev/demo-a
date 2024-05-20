import streamlit as st
from spleeter_page import show_spleeter_page
from cover_song_analyzer_page import show_cover_song_analyzer_page

st.set_page_config(page_title="Audio Processing App", layout="wide")

# Navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Select a page:', ['Spleeter', 'Cover Song Analyzer'])

# Page routing
if page == 'Spleeter':
    show_spleeter_page()
elif page == 'Cover Song Analyzer':
    show_cover_song_analyzer_page()
