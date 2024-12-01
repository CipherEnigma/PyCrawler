import streamlit as st
from scrape import (scrape_website,
                    split_dom_content,
                    clean_body_content,
                    extract_body_content,
                    )
from parse import parse_with_ollama
# Initialize session state
if "dom_content" not in st.session_state:
    st.session_state.dom_content = ""

# Set page title
st.title("PyCrawler AI Web Scraper")

# Add some descriptive text
st.write("Enter a URL below to start scraping")

# URL input
url = st.text_input("Enter the URL")

# Add a debug message to ensure values are being captured
if url:
    st.write(f"You entered: {url}")

# Scrape button
if st.button("Scrape Site"):
    st.write("Scraping site...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
   
    st.session_state.dom_content = cleaned_content
    with st.expander("Show DOM content"):
        st.write(st.session_state.dom_content)

# Description box
parse_description = st.text_area("Describe what you want to parse")

# Parse button
if st.button("Parse Content"):
    if parse_description:
        st.write("Parsing content...")
        dom_chunks = split_dom_content(st.session_state.dom_content)
        result = parse_with_ollama(dom_chunks, parse_description)
        st.write(result)