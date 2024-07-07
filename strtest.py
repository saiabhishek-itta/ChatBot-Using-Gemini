import streamlit as st

# Title of the application
st.title('Chat Application')

# Initialize session state if not already done
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Text input for user message
user_message = st.text_input('You:', value=st.session_state.get('input', ''))

# Button to send message
if st.button('Send'):
    if user_message:
        # Append user message to chat history
        st.session_state.messages.append(('You', user_message))

        # Here you can implement your chatbot response logic
        # For this example, we just echo the user message
        bot_response = f"Echo: {user_message}"
        st.session_state.messages.append(('Bot', bot_response))

        # Clear the input field by resetting the value in session state
        st.session_state.input = ''

# Display chat history
for sender, message in st.session_state.messages:
    st.write(f"{sender}: {message}")



