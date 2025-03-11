import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key="AIzaSyDbVzN7R8Bwd9iWLWC8g8P5cqFMx8My33o")

# Initialize memory for conversation history
memory = ConversationBufferMemory()

# Streamlit UI
st.title("🤖 AI Data Science Tutor")
st.write("Ask me anything about Data Science!")

# User input
user_input = st.text_input("Enter your question:")

def get_gemini_response(prompt):
    """Generate AI response using Gemini 1.5 Pro"""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text

# Chatbot logic
if user_input:
    # Retrieve memory
    conversation_history = memory.load_memory_variables({})["history"]
    
    # Create the conversation prompt
    prompt = f"Conversation so far:\n{conversation_history}\n\nUser: {user_input}\nAI:"
    
    # Get AI response
    ai_response = get_gemini_response(prompt)

    # Store in memory
    memory.save_context({"input": user_input}, {"output": ai_response})
    
    # Display response
    st.write("**AI Tutor:**", ai_response)

# Clear chat button
if st.button("Clear Chat"):
    memory.clear()
    st.rerun()  # Updated from `st.experimental_rerun()`
