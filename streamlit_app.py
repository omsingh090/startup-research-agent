import streamlit as st
from agent import run_agent

st.title("Startup Research Assistant Agent")

query = st.text_input("Enter your query")

if query:

    st.write("Query received!")

    try:

        result = run_agent(query)

        st.write(result)

    except Exception as e:

        st.error(f"Error: {str(e)}")