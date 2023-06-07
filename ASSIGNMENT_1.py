import streamlit as st
import speech_recognition as sr

def transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        st.write("Transcription:", text)
    except sr.UnknownValueError:
        st.write("Could Not Understand")
    except sr.RequestError as e:
        st.write("Error occurred: ", e)

def main():
    st.title("Real-time Voice Transcription")

    # Start/Stop buttons
    start_button = st.button("Start Transcription")
    stop_button = st.button("Stop Transcription")

    # Text area to display transcription
    st.write("Transcription:")
    transcript_area = st.empty()

    if start_button:
        transcribe_audio()

    if stop_button:
        st.stop()

if __name__ == '__main__':
    main()
