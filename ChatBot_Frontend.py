import streamlit as st
import time
from ChatBot_Backend import chatbot,retrival_all_thread
from langchain_core.messages import HumanMessage,AIMessage
import uuid
def generate_thread():
    thread_id = uuid.uuid4()
    return thread_id


def reset_chat():
    thread_id = generate_thread()
    st.session_state['thread_id'] = thread_id
    add_thread(thread_id)
    st.session_state['message_history'] = []


def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)


def load_conversation(thread_id):
    state = chatbot.get_state(
        config={
            'configurable': {
                'thread_id': thread_id
            }
        }
    )

    return state.values.get('messages', [])

def get_chat_title(thread_id):
    messages = load_conversation(thread_id)

    for msg in messages:
        if isinstance(msg, HumanMessage):
            title = msg.content.strip()

            # Keep sidebar title short
            if len(title) > 30:
                title = title[:30] + "..."

            return title

    return "New Chat"

# Initialize session state

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread()


if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrival_all_thread()


add_thread(st.session_state['thread_id'])

st.sidebar.title('Nexora')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
    chat_title = get_chat_title(thread_id)
    if st.sidebar.button(chat_title,key=str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({'role': role, 'content': msg.content})

        st.session_state['message_history'] = temp_messages

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}
    # first add the message to message_history
    with st.chat_message('assistant'):
        with st.spinner("Thinking...."):
            ai_message =st.write_stream(
                #ADD STREAMING
            chunk.content for chunk,metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]}, 
                config=CONFIG,
                stream_mode='messages'
                ))
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})