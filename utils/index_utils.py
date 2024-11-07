# utils/index_utils.py

import tempfile
import pymupdf4llm
from llama_index.core import VectorStoreIndex

def create_index_from_files(uploaded_files):
    """Create a VectorStoreIndex from multiple PDF files using PyMuPDF4LLM."""
    documents = []
    llama_reader = pymupdf4llm.LlamaMarkdownReader()

    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getbuffer())
            tmp_file_path = tmp_file.name

        # Load documents from each file
        file_documents = llama_reader.load_data(tmp_file_path)
        documents.extend(file_documents)

    # Create the index from all documents
    index = VectorStoreIndex.from_documents(documents)
    return index
