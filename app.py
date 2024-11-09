## Create a Q&A Application for fetching results from Web URL using Nvidia

import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.output_parsers import StrOutputParser

## loading Nvidia API Key
os.environ['NVIDIA_API_KEY'] = os.getenv("NVIDIA_API_KEY")

## load the LLM model
llm = ChatNVIDIA(model="meta/llama3-70b-instruct")



def fetch_result():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = NVIDIAEmbeddings()
        st.session_state.loader = WebBaseLoader("https://www.geeksforgeeks.org/natural-language-processing-overview/")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splits = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
        st.session_state.final_text_splits = st.session_state.text_splits.split_documents(st.session_state.docs[:30])
        st.session_state.vector_store = FAISS.from_documents(st.session_state.final_text_splits, st.session_state.embeddings)

## Streamlit App
st.set_page_config(page_title="Nvidia NIM Q&A - Website URL", page_icon="🚀")
st.title("Nvidia NIM Q&A - Website URL 🚀")

prompt = ChatPromptTemplate.from_template(
""" 
Answer the questions based on provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Question:{input}

"""
)

prompt_1 = st.text_input("Enter your question from URL your provided")

if st.button("Fetch Answer"):
    fetch_result()
    st.success("FAISS Vector Store DB is Ready using NvidiaEmbedding!!!")


import time
if prompt_1:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vector_store.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt_1})
    print("Response time :", time.process_time()-start)
    st.write(response['answer'])


    ## With streamlit expander
    with st.expander("Document Similarity Search"):
        # find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("------------------------------")

    






