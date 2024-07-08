import streamlit as st
from chat import askquestion


with st.sidebar:
    #openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "TRAVLR Chatbot"
    "[View the source code](https://github.com/saiabhishek-itta/ChatBot-Using-Gemini)"


st.title("Travlr Chatbot")
st.caption("Here to assist all your travel queries")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    #if not openai_api_key:
        #st.info("Please add your OpenAI API key to continue.")
        #st.stop()

    #client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response =askquestion(prompt)
    msg = response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)