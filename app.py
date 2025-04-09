import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="🔎 RAG-powered Multi-Agent App",
    layout="wide",
    page_icon="🤖"
)

st.title("🔎 Search + QA Agents")
st.markdown("""
#### Multi-Doc QA Bot with RAG  
Upload multiple documents → Ask questions, get citations from the relevant doc.
""")

with st.expander("🧠 Try Multi-Document QA"):
    st.file_uploader("Upload your documents", type=["pdf", "txt", "docx"], accept_multiple_files=True)
    st.text_input("Ask a question about the documents")
    st.button("Answer")  # Placeholder for actual logic

st.markdown("""
#### Website Chat Agent (with RAG from URL)  
Enter a URL → Agent scrapes content and answers based on the website data.
""")

with st.expander("🌐 Try Website QA"):
    st.text_input("Enter a website URL")
    st.text_input("Ask a question about the website")
    st.button("Answer from Website")  # Placeholder for website QA logic

st.markdown("""
#### GitHub Repo Assistant  
Input a GitHub repo URL → clone, parse README, code files → ask questions about the code.
""")

with st.expander("🐙 Try GitHub QA"):
    st.text_input("Enter GitHub repo URL")
    st.text_input("Ask a question about the repo")
    st.button("Answer from Repo")  # Placeholder for GitHub QA logic

st.markdown("---")
st.info("This is a prototype. Add API integrations and backend logic to enable full RAG capabilities.")
