# DocuQuery with Llama3 and Groq Demo

This Streamlit application demonstrates the integration of ChatGroq (Llama3 model), OpenAIEmbeddings, and FAISS for document embedding and retrieval. Users can input questions, and the app retrieves relevant documents and provides accurate responses based on the provided context.

## Features

- **Document Embedding**: Embed documents using OpenAI embeddings and store them using FAISS.
- **Question Answering**: Answer user questions based on embedded documents using ChatGroq's Llama3 model.
- **Document Similarity Search**: Display similar documents related to the user's query.

## Installation

To run this application locally, follow these steps:

1. Prerequisites

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- [Git LFS](https://git-lfs.github.com/)
- OpenAI API key
- Groq API key


2. Clone the Repository

    ```sh
    git clone https://github.com/Tobsky/DocuQuery
    cd yourrepository

3. Set Up Environment Variables

    Create a .env file in the root directory of the project and add your OpenAI and Groq API keys:

    ```sh
    OPENAI_API_KEY=your_openai_api_key
    GROQ_API_KEY=your_groq_api_key

4. Install Dependencies
    ```sh
    pip install -r requirements.txt

5. Run the Application
    ```sh
    streamlit run app.py

## Usage

1.  Embedding Documents: Click the "Embed Documents" button to      process and embed the documents located in the ./PDFdocs directory.
2.  Ask a Question: Enter your question in the text input field and press Enter. The app will retrieve relevant documents and provide an answer based on the context.
3.  View Similar Documents: Expand the "Document Similarity Search" section to view similar documents related to your query.

## Code Overview

### Main Components
1. Environment Setup: Load API keys from the .env file using dotenv.
2. Document Embedding: Embed documents using OpenAI embeddings and store them with FAISS.
3. Question Answering: Use ChatGroq's Llama3 model to answer questions based on the provided context.
4. Streamlit Interface: Provide a user interface to embed documents, ask questions, and view similar documents.

### Key Functions
1. vector_embedding(): Handles document embedding and vector store creation.
2. create_stuff_documents_chain(): Combines documents to form a chain for processing.
3. create_retrieval_chain(): Creates a retrieval chain to fetch relevant documents based on user queries.

## Troubleshooting

### Common Errors
1. Rate Limit Error: If you exceed the API quota, consider upgrading your OpenAI plan or reducing the number of API calls.
2. Environment Variable Errors: Ensure your .env file is correctly set up with valid API keys.
3. Document Loading Issues: Verify that the document directory (./PDFdocs) exists and contains valid PDF files.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.
