import streamlit as st

def show_spleeter_page():
    st.title('Spleeter: Separate Vocals and Instrumentals')
    st.write('Upload an audio file and we will separate the vocals and instrumentals.')

    uploaded_file = st.file_uploader("Choose an audio file...", type=['wav', 'mp3', 'ogg'])

    if uploaded_file is not None:
        st.audio(uploaded_file)
        st.info('Processing the audio... Please wait for the backend to process your file.')
        st.download_button('Download Vocals', "", file_name='vocals.wav')
        st.download_button('Download Instrumentals', "", file_name='instrumentals.wav')
