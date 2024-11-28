import streamlit as st
from gtts import gTTS
import base64

# Function to autoplay audio using base64 encoding
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# Streamlit UI
st.title("Text-to-Speech with gTTS")

user_input = st.text_area("Enter text:")

if st.button("Convert to Speech"):
    if user_input:
        # Convert text to speech with fast speed (slow=False)
        tts = gTTS(user_input, lang='en', slow=False)
        output_file = "output.mp3"
        tts.save(output_file)

        # Play the audio using Streamlit's audio player
        st.audio(output_file, format="audio/mp3")

        # Autoplay the audio using base64 encoding (in the browser)
        autoplay_audio(output_file)

    else:
        st.warning("Please enter some text to convert to speech.")
