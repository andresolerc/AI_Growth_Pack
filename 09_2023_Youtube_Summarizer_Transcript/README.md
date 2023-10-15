
# YouTube Video Summarizer

## Overview

The YouTube Video Summarizer is an application built with Streamlit that takes a YouTube URL as input and provides a summarized version of the video's transcript. The app leverages the `langchain` library, which internally uses OpenAI's GPT-3.5 Turbo model for the summarization.

## Features

1. **YouTube URL Input**: Users can provide a link to a YouTube video to fetch its transcript.
2. **Language Selection**: Allows users to select from multiple languages to retrieve the appropriate transcript.
3. **Transcript Summarization**: The full transcript is broken down into chunks, which are then summarized using the OpenAI model.
4. **Downloadable Results**: Both the full transcript and its summary can be downloaded as text files.

## Getting Started

### Prerequisites

1. Python environment.
2. OpenAI API key.

### Installation

1. Create a virtual environment:
```bash
python -m venv myenv
```

2. Activate the virtual environment:
- On macOS/Linux:
```bash
source myenv/bin/activate
```
- On Windows:
```bash
myenv\Scripts\activate
```

3. Install the required libraries:
```bash
pip install streamlit langchain youtube-transcript-api openai tiktoken
```

4. Run the app:
```bash
streamlit run yt_summary_app.py
```

### Usage

1. Enter a valid YouTube URL in the provided input box.
2. Select the languages to consider for the transcript.
3. Click on "Run Summarization".
4. Once the summarization is complete, you can view the summary and the full transcript.
5. Both the summary and the transcript can be downloaded using the provided download buttons.

## Note

Make sure to replace the placeholder `"YOUR_OPENAI_API_KEY"` with your actual OpenAI API key in the `yt_summary_app.py` file.

## 📝 Why I Share This? 

Langchain is a powerful framework for working with multiple LLMs. Whether you want to extract information from a video, mapping out a collection of videos, or summarizing videos for later to chat with them, Langchain simplifies the process.

## 👩‍💻 Want to take action? 

Drop a comment or send me a message! Always happy to chat about Python and Langchain.

## Andy Soler

P.S. If you're excited about unlocking the potential of AI for your career, you're not alone. Every week, I share actionable insights and steps on leveraging AI for career advancement. It's a quick read that could make all the difference in your professional journey. Be part of an active community of over 1200+ professionals who are all focused on harnessing the power of AI. 👇 

https://bit.ly/3r9p2Do

#machinelearning #artificialintelligence #technology #amsterdam #careers #innovation #python #business #dataengineering #hr #coaching

