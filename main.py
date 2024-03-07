import streamlit as st
import langchain_helper as lch

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key="my_from"):
        youtube_url = st.sidebar.text_area(
            label="What is the url of the youtube video?", max_chars=80
        )
        query = st.sidebar.text_area(
            label="Ask me about the video?", max_chars=50, key="query"
        )
        submit_button = st.form_submit_button(label="Submit")

if query and youtube_url:
    db = lch.create_vector_db_from_youtube_url(youtube_url)
    response, docs = lch.get_response_from_query(db, query)
    st.subheader("Answer:")
    st.text(response["docs"])
