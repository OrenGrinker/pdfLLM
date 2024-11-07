# app.py

import streamlit as st
import openai
from utils.index_utils import create_index_from_files
from utils.query_utils import answer_question

# Import OpenAI for model selection
from llama_index.llms.openai import OpenAI

def main():
    st.title("PDF Question Answering App")

    # Sidebar for configuration
    st.sidebar.header("Configuration")

    # Option to input API key in the sidebar
    api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")
    if api_key:
        openai.api_key = api_key

    # Dropdown to choose between models in the sidebar
    model = st.sidebar.selectbox(
        "Choose a model",
        options=["gpt-4o", "gpt-4o-mini", "gpt-4"],
        index=0
    )

    # File uploader for multiple PDF files (up to 5) in the sidebar
    uploaded_files = st.sidebar.file_uploader(
        "Upload PDF files (max 5)",
        type="pdf",
        accept_multiple_files=True
    )

    # Initialize session state for index and conversation history
    if "index" not in st.session_state:
        st.session_state.index = None
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    # Create index only once when files are uploaded
    if uploaded_files:
        if len(uploaded_files) > 5:
            st.sidebar.error("You can upload a maximum of 5 files.")
        elif st.session_state.index is None:  # Only create index if it hasn't been created yet
            with st.spinner('Creating index from uploaded files...'):
                st.session_state.index = create_index_from_files(uploaded_files)
                st.success('Index created.')

    # Question input (main content area)
    question = st.text_input("Ask a question about the uploaded PDF content")

    if question and st.session_state.index:
        # Append question to history
        st.session_state.conversation_history.append({"role": "user", "content": question})

        # Generate answer
        with st.spinner('Generating answer...'):
            answer = answer_question(st.session_state.index, question, model)
            st.success('Answer generated.')

        # Append answer to history
        st.session_state.conversation_history.append({"role": "assistant", "content": answer})

        # Display the question and answer
        st.write("**Question:**", question)
        st.write("**Answer:**", answer)

        # Display conversation history
        st.subheader("Conversation History")
        for i, turn in enumerate(st.session_state.conversation_history):
            if turn["role"] == "user":
                st.write(f"**Q{i//2 + 1}:** {turn['content']}")
            else:
                st.write(f"**A{i//2 + 1}:** {turn['content']}")

    # Footer in the sidebar
    st.sidebar.markdown(
        """
        <div style="position: absolute; margin-top: 30px; width: 100%; text-align: center; font-size: 14px;">
            💻 Created by Oren Grinker
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
