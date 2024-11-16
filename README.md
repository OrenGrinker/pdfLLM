# PDF Question Answering App

This is a **Streamlit-based application** that allows users to upload multiple PDF files and ask questions about their content. The application uses **OpenAI language models** to interpret queries and provide answers based on the uploaded PDFs. The app employs a vector-based index to enhance the question-answering capabilities on multi-page or multi-document PDFs.

## Features

- **Multi-Document Upload**: Upload up to 5 PDF files simultaneously.
- **Model Selection**: Choose between different OpenAI language models for custom performance.
- **Dynamic Index Creation**: Automatically creates an index from uploaded PDFs to enable efficient querying.
- **Interactive Q&A**: Enter questions and receive detailed answers based on the document content.
- **Conversation History**: Track past questions and answers within the session.

## Requirements

- **Python 3.8+**
- **Streamlit**
- **OpenAI API Key**
- **PyMuPDF4LLM**
- **LlamaIndex**

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/OrenGrinker/pdfLLM.git
   cd pdfLLM
    ```

2. **Install Dependencies**

   Make sure you have pip installed. Run the following command to install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   
3.**Set Up OpenAI API Key**

   The app requires an OpenAI API key to function. You will be prompted to enter your API key when running the application.

## Usage

1. **Run the Application**

   Start the app by running the following command:
   ```bash
   streamlit run app.py
    ```
   
2. **Upload PDF Files**

   In the sidebar, you can upload up to 5 PDF files. The app will create an index for efficient querying.

3. **Ask Questions**

   Enter questions in the main content area, and the app will retrieve answers based on the content of the uploaded PDFs.

4. **Choose Model**
   Select a model from the sidebar (e.g., gpt-4o, gpt-4o-mini, or gpt-4) to adjust response specificity and speed.

## Code Structure

- app.py: Main file that initializes the Streamlit app, sets up user interface components, and handles interactions.
- utils/index_utils.py: Contains functions to create a vector-based index from uploaded PDFs.
- utils/query_utils.py: Provides functions to query the index and retrieve answers based on user input.

## Example Workflow

- Upload your PDF files in the sidebar.
- Choose the desired model for response generation.
- Ask questions about the content of the PDFs in the main input field.
- View answers and scroll through conversation history to see previous queries and responses.

## Contributing

Feel free to open issues or submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
