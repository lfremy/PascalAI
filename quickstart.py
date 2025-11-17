# app.py
import streamlit as st
from prompt_pascal import V4_RIGOUREUX
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

st.title("💭 Dialoguer avec Pascal")
st.caption("Blaise Pascal (1623-1662)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Posez votre question à Pascal..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=600,
            system=V4_RIGOUREUX,
            messages=[{"role": m["role"], "content": m["content"]} 
                     for m in st.session_state.messages]
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})