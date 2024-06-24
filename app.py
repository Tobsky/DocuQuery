import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Load the Groq and Openai API Key
os.environ['OPENAI_API_KEY'] =os.getenv('OPENAI_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')

# Streamlit app title
st.title('DocuQuery using Llama3 and Groq')

# Initialize the language model
llm = ChatGroq(groq_api_key = groq_api_key,
                model_name = "Llama3-8b-8192")

# Define the prompt template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Questions:{input}
    """
)

#@st.cache # Cache for later use by the client code when the template is loaded
def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = OpenAIEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader("./PDFdocs") # Data Ingestion
        st.session_state.docs =st.session_state.loader.load() # Document Loading
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # Chunck creation
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50]) # Splitting
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings) # Vector embeddings

# Input field for user questions
prompt1 = st.text_input("Enter Your Question From Documents")

# Button to trigger document embedding
if st.button("Documents Embedding"):
    with st.spinner("Embedding documents..."):
        try:
            vector_embedding()
            st.write("Vector Store DB Is Ready")
        except Exception as e:
            st.error(f"An error occurred during vector embedding: {e}")

# Processing user question and fetching relevant documents
if prompt1:
    try:
        document_chain =create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vectors.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        
        start = time.process_time()
        response = retrieval_chain.invoke({'input': prompt1})
        response_time = time.process_time() - start
        
        st.write(f"Response time: {response_time:.2f} seconds")
        st.write(response['answer'])

        # Display similar documents in an expander
        with st.expander("Document Similarity Search"):
            # Find the relevant chunks
            for i, doc in enumerate(response['context']):
                st.info(doc.page_content)
                st.write("--------------------------------")
    except Exception as e:
        st.error(f"An error occurred during document retrieval: {e}")
