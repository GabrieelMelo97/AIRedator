"""
Main Streamlit application for text evaluation.
This module handles the web interface and integration with the evaluation system.
"""

import logging
import sys
from pathlib import Path
from typing import List, Dict

import streamlit as st

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.backend.workflows import grade_essay

class TextEvaluationApp:
    """Main class for the text evaluation Streamlit application."""
    
    def __init__(self):
        """Initialize the Streamlit application settings."""
        self._configure_page()
        self._initialize_session_state()
        
    def _configure_page(self) -> None:
        """Configure the Streamlit page settings."""
        st.set_page_config(
            page_title="📝 Essay Evaluator",
            page_icon="📝",
            layout="wide"
        )
        
    def _initialize_session_state(self) -> None:
        """Initialize the session state for message history."""
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": "What essay would you like me to evaluate today?"
                }
            ]
    
    @staticmethod
    def clear_chat_history() -> None:
        """Clear the chat history in the session state."""
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "What essay would you like me to evaluate today?"
            }
        ]
        logger.info("Chat history cleared")
    
    def display_chat_messages(self) -> None:
        """Display all messages in the chat history."""
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
    
    @staticmethod
    def generate_evaluation_response(text_input: str) -> str:
        """
        Generate evaluation response for the input text.
        
        Args:
            text_input (str): The text to be evaluated
            
        Returns:
            str: The evaluation result
        """
        try:
            logger.info("Generating evaluation for input text")
            result = grade_essay(text_input)
            
            # Format the response with scores
            response = f"""
            🔹 Evaluation Results 🔹\n\n
            🎯 Final Score: {result['final_score'] * 10:.2f}/10\n
            📌 Relevance: {result['relevance_score'] * 10:.2f}/10\n
            ✍️ Grammar: {result['grammar_score'] * 10:.2f}/10\n
            📖 Structure: {result['structure_score'] * 10:.2f}/10\n
            🔍 Depth: {result['depth_score'] * 10:.2f}/10
            """
            return response
        except Exception as e:
            logger.error(f"Error generating evaluation: {str(e)}")
            return "An error occurred while evaluating the text. Please try again."
    
    def handle_user_input(self) -> None:
        """Handle user input and generate responses."""
        if prompt := st.chat_input():
            # Add user message to chat
            self._add_message("user", prompt)
            
            # Generate and display assistant response
            with st.chat_message("assistant"):
                with st.spinner("Analyzing..."):
                    response = self.generate_evaluation_response(prompt)
                    self._display_streaming_response(response)
            
            # Add assistant response to chat history
            self._add_message("assistant", response)
    
    def _add_message(self, role: str, content: str) -> None:
        """
        Add a message to the chat history.
        
        Args:
            role (str): The role of the message sender
            content (str): The message content
        """
        st.session_state.messages.append({"role": role, "content": content})
        if role == "user":
            with st.chat_message(role):
                st.write(content)
    
    def _display_streaming_response(self, response: str) -> None:
        """
        Display the response in a streaming fashion.
        
        Args:
            response (str): The response to display
        """
        placeholder = st.empty()
        full_response = ''
        
        for item in response:
            full_response += item
            placeholder.markdown(full_response)
        placeholder.markdown(full_response)
    
    def setup_sidebar(self) -> None:
        """Setup the sidebar with controls and information."""
        with st.sidebar:
            st.title("📝 Essay Evaluator")
            st.markdown("""
            ### About
            This application evaluates essays considering:
            - Topic Relevance
            - Grammar
            - Structure
            - Argument Depth
            
            Type your essay in the chat field to start the evaluation.
            """)
            st.button('Clear History', on_click=self.clear_chat_history)
    
    def run(self) -> None:
        """Run the Streamlit application."""
        try:
            self.setup_sidebar()
            self.display_chat_messages()
            self.handle_user_input()
        except Exception as e:
            logger.error(f"Application error: {str(e)}")
            st.error("An error occurred in the application. Please reload the page.")

def main():
    """Main entry point for the application."""
    app = TextEvaluationApp()
    app.run()

if __name__ == "__main__":
    main() 