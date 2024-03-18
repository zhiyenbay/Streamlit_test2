import streamlit as st
from transformers import SeamlessM4Tv2ForSpeechToText
# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version January 2023

from st_audiorec import st_audiorec
from transformers import SeamlessM4Tv2Model, AutoProcessor
import torch

# device = "cuda:0" if torch.cuda.is_available() else "cpu"
# processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
# model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large")

# process input
# audio_inputs = processor(audios=audio_sample["array"], return_tensors="pt").to(device)

import speech_recognition as sr



# DESIGN implement changes to the standard streamlit UI/UX
# --> optional, not relevant for the functionality of the component!
st.set_page_config(page_title="AI Medical Assistant")
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
            unsafe_allow_html=True)
# Design change st.Audio to fixed height of 45 pixels
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
            unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # lightmode


def audiorec_demo_app():

    # TITLE and Creator information
    st.title('Запись аудио для заполнения анкеты Лист оценки риска по Морзе ')
    st.markdown('Implemented by 3MIS')
    st.write('\n\n')

    # TUTORIAL: How to use STREAMLIT AUDIO RECORDER?
    # by calling this function an instance of the audio recorder is created
    # once a recording is completed, audio data will be saved to wav_audio_data

    wav_audio_data = st_audiorec() 

    # add some spacing and informative messages
    col_info, col_space = st.columns([0.57, 0.43])
    with col_info:
        st.write('\n')  # add vertical spacer
        st.write('\n')  # add vertical spacer
        st.write('The .wav audio data, as received in the backend Python code,'
                 ' will be displayed below this message as soon as it has'
                 ' been processed. [This informative message is not part of'
                 ' the audio recorder and can be removed easily] 🎈')

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
            r = sr.Recognizer()
            audio = r.record(sr.AudioFile((wav_audio_data))
            s = r.recognize_google(audio)
            st.write("Text: "+s)            
            # try:
            #     s = r.recognize_google(audio)
            #     st.write("Text: "+s)
            # except Exception as e:
            #     st.write("Exception: "+str(e))


if __name__ == '__main__':
    # call main function
    audiorec_demo_app()
