import streamlit as st 

upload_file = st.file_uploader("upload PDF",
                               type="pdf",
                               accept_multiple_files=True)


# chatbot skeleton

user_query = st.text_area("enter your querry", height=150, placeholder="Ask anything")

question_button = st.button("Ask AI Lawyer")

dummy_response = "this is a dummy response"
if question_button:
    if upload_file:
        st.chat_message("user").write(user_query)
        st.chat_message("AI Lawyer").write(dummy_response)

    else:
        st.error("Kindly upload your files")