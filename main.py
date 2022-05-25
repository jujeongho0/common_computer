import streamlit as st
from streamlit_chat import message
import requests

st.header("dialogpt API를 이용한 영어 챗봇")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input = st.text_input("당신: ", key="input")

if user_input:

    url = "https://main-openchat-fpem123.endpoint.ainize.ai/send/jeongho"
    data = {
        "bot_id": "",
        "topic": "",
        "text": user_input,
        "agent": "dialogpt.medium"
    }

    response = requests.post(url, data=data)
    answer = response.json()['output']

    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
