# Install Streamlit if you haven't already
# !pip install streamlit
# !pip install yt-dlp
# !pip install -U openai-whisper
# !pip install git+https://github.com/openai/whisper.git 
# Fmpeg is required on your system for yt-dlp merge to work. You can install it via cmd: brew install ffmpeg
# Use the browser's Developer Tools > Network to search for these "master or manifest m3u8" (HLS manifest) URL in Chrome browser for this app

import streamlit as st
import whisper
import subprocess
import re
import tempfile # for creating a temporary audio file
import os

# Initialize the transcript variable globally
transcript = ""

def main(): 
    st.title("AI Media Processing App")

    # URL testing 
    #url = "https://hls.ted.com/project_masters/8549/manifest.m3u8?intro_master_id=2346"  # Replace with actual video URL
    #format_options = get_video_formats(url)

    #if format_options:
    #    st.write("Available formats:", format_options)
    #else:
    #    st.write("No available formats found or there was an error fetching the formats.")
    # End - URL testing

    # UI component to select the audio file
    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    # In the Streamlit app, call this function with the uploaded file
    if st.button("Transcribe Audio", key="transcribe_button"):
        if audio_file is not None:    
            transcribe_audio(audio_file)
            st.markdown("**Open a new chat in ChatGPT and paste the prompt below:**")
            multi = '''You are an expert English book reader. 
            You are an expert content creator with skills in storytelling and copywriting. 
            You will read the provided transcript speech attached and describe it into a detailed and organized markdown document. 

            1. **Segmentation:** Break down the transcript into smaller, more manageable segments. 
               Focus on one section at a time to ensure each part receives the necessary attention for accurate markdown formatting. 

               **Topic Sentence (TS)** - *the beginning.* Needs to state ONE idea clearly

               **Supporting Sentences (SS)** - *the middle.* Elaborates and explains the idea introduced in the topic sentence Provides evidence and examples. 
               Explains the evidence or example included - why is it relevant?

               **Concluding Sentence (CS)** - *the end*
               
            2. **Thematic Analysis:** Identify key themes, topics, and ideas within each segment. 
               This will help in structuring the markdown document with appropriate headings and subheadings.
            '''
            st.markdown(multi)
            st.write("Transcription:", transcript)

    
    # Sidebar for inputs and settings
    with st.sidebar:
        st.header("Settings")
        
        st.header("Download Media")
        # Text box for video URL
        video_url = st.text_input("Enter the video URL:")
        format_options = []  # Initialize format_options here

        # Fetch and display format options
        if video_url:
            formats = get_video_formats(video_url)  # Call the function without 'media_type'

            if formats['audio']:  # Check if the list is not empty
                audio_format_selected = st.select_slider("Select Audio Format", options=formats['audio'])
            else:
                st.error("No audio formats found.")

            if formats['video']:  # Check if the list is not empty
                video_format_selected = st.select_slider("Select Video Format", options=formats['video'])
            else:
                st.error("No video formats found.")

            # Streamlit UI button logic
            if st.button("Download Audio"):
                download_media(video_url, None, audio_format_selected, 'audio')

            if st.button("Download Video"):
                download_media(video_url, video_format_selected, None, 'video')

            merge_media = st.checkbox("Merge video and audio")
        
            if merge_media and st.button("Download Merged Media"):
                download_media(video_url, video_format_selected, audio_format_selected, 'merge')


def get_video_formats(video_url):
    command = f"yt-dlp --list-formats {video_url}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        error_message = stderr.decode().strip()
        st.error(f"Error fetching formats: {error_message}")
        return {'video': [], 'audio': []} # Return early if there's an error

    # Continue processing if no error occurred
    output = stdout.decode()
    format_lines = [line.strip() for line in output.split('\n') if line.strip()]

    formats = {'video': [], 'audio': []}
    for line in format_lines:
        match = re.match(r'^(\w+-\w+|\d+)\s+(.*?)\s+.*?$', line)
        if match:
            format_code, format_description = match.groups()
            if "audio only" in line:
                formats['audio'].append(f"{format_code}: {format_description}")
            elif "video only" in line or "x" in line:
                formats['video'].append(f"{format_code}: {format_description}")

    return formats


def download_media(video_url, video_format, audio_format, download_type):
    if download_type == 'audio':
        command = f"yt-dlp -f {audio_format.split(':')[0].strip()} {video_url} -x --audio-format mp3"
    elif download_type == 'video':
        command = f"yt-dlp -f {video_format.split(':')[0].strip()} {video_url}"
    elif download_type == 'merge':
        command = f"yt-dlp -f '{video_format.split(':')[0].strip()}+{audio_format.split(':')[0].strip()}' {video_url}"
    
    try:
        subprocess.run(command, shell=True, check=True)
        st.success(f"Download completed successfully for: {download_type}")
    except subprocess.CalledProcessError as e:
        st.error(f"An error occurred during download: {e}")

#Whisper audio section

def transcribe_audio(uploaded_file):
    global transcript  # Use the global transcript variable
    
    # Load the Whisper model
    model = whisper.load_model("base")

    # Save the uploaded file to a temporary file
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.getvalue())

    # Transcribe the audio from the saved file
    result = model.transcribe("temp_audio.mp3")
    transcript = result["text"]

    # Save the transcription to a local file
    filename = "transcript.txt"
    with open(filename, "w") as file:
        file.write(transcript)

    return transcript


if __name__ == "__main__":
    main()

