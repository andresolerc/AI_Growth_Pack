import streamlit as st
from langchain.document_loaders import YoutubeLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import TokenTextSplitter

# Streamlit App
st.title('YouTube Video Summarizer')

# User input
youtube_url = st.text_input('Enter YouTube URL:', '')
languages = st.multiselect('Select Languages:', options=['en', 'en-US', 'es', 'fr'], default=['en', 'en-US'])

# Initialize session state variables if they don't exist
if 'summary' not in st.session_state:
    st.session_state.summary = ""
if 'transcript' not in st.session_state:
    st.session_state.transcript = ""

# Run button
if st.button('Run Summarization'):
    try:
        with st.spinner('Loading transcript...'):
            # Load Transcript
            loader = YoutubeLoader.from_youtube_url(youtube_url, language=languages)
            transcript = loader.load()

        if transcript:
            with st.spinner('Splitting transcript...'):
                # Split Transcript
                splitter = TokenTextSplitter(model_name="gpt-3.5-turbo-16k", chunk_size=10000, chunk_overlap=100)
                chunks = splitter.split_documents(transcript)

            with st.spinner('Summarizing...'):
                # Set up LLM
                openai_api_key = "YOUR_OPENAI_API_KEY"
                llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-3.5-turbo-16k", temperature=0.3)

                # Summarize
                summarize_chain = load_summarize_chain(llm=llm, chain_type="refine", verbose=True)
                summary = summarize_chain.run(chunks)
                
                st.session_state.summary = summary
                st.session_state.transcript = '\n'.join(map(str, transcript))

            st.success('Summarization complete.')

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display and Download summary
if st.session_state.summary:
    st.subheader('Summary:')
    st.write(st.session_state.summary)
    st.download_button(
        label="Download Summary",
        data=st.session_state.summary.encode(),
        file_name="summary.txt",
        mime="text/plain"
    )

# Display and Download transcript
if st.session_state.transcript:
    st.subheader('Transcript:')
    st.write(st.session_state.transcript)
    st.download_button(
        label="Download Transcript",
        data=st.session_state.transcript.encode(),
        file_name="transcript.txt",
        mime="text/plain"
    )

            

            

   
