import streamlit as st
from vector_database import upload_pdf , load_pdf , pdfs_directory, create_chunks, FAISS_DB_PATH, ollama_model_name, create_vector_store
from rag_pipeline import *

uploaded_file = st.file_uploader("Upload PDF",
                                 type="pdf",
                                 accept_multiple_files=False)


#Step2: Chatbot Skeleton (Question & Answer)

user_query = st.text_area("Enter your prompt: ", height=150 , placeholder= "Ask Anything!")

ask_question = st.button("Ask AI Lawyer")

if ask_question:

    if uploaded_file and user_query:
        upload_pdf(uploaded_file)
        documents = load_pdf(pdfs_directory + uploaded_file.name)
        text_chunks = create_chunks(documents)
        faiss_db = create_vector_store(FAISS_DB_PATH, text_chunks, ollama_model_name)

        retrieved_docs=retrieve_docs(faiss_db, user_query)
        response=answer_query(documents=retrieved_docs, model=llm_model, query=user_query)

        st.chat_message("user").write(user_query)
        st.chat_message("AI Lawyer").write(response) 
    else:
        st.error("Kindly upload a valid PDF file and/or ask a valid Question!")