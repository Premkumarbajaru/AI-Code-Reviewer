import streamlit as st
import google.generativeai as ai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load API Key securely
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if API key is available
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY environment variable not found. Please set it first.")
    st.stop()

# Configure API key
ai.configure(api_key=GOOGLE_API_KEY)

# Define system prompt
system_prompt = """You are an AI-powered Code Reviewer.  
Your primary role is to analyze submitted code, detect every possible issue, and provide detailed feedback.  

You should:  
1. Identify syntax errors, including indentation issues, missing colons, and incorrect indentation levels.  
2. Detect runtime errors such as undefined variables, type mismatches, and division by zero.  
3. Find logical errors like incorrect conditions, infinite loops, and miscalculations.  
4. Suggest best practices and performance optimizations, including efficient loops, better data structures and algorithms, and improved readability.  

For each issue:  
- Provide a clear explanation of why it is a problem.  
- Suggest a corrected version of the code with proper indentation, best practices, and efficiency improvements.  

Format your response using markdown with:
- Clear section headings (##)
- Code blocks (```python)
- Bullet points for issues
- Bold text for error types
"""

# GenerativeModel Initialization
model = ai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

# Streamlit UI design
st.title(":speech_balloon: AI Code Reviewer")
st.markdown("Enter your code below to get a detailed review and suggestions for improvement.")

# Input area for code
query = st.text_area(
    "Enter Your Code Here...",
    height=300,
    placeholder="Paste your code here for analysis..."
)

# Analyze button
btn_click = st.button("Analyze Code")

# Clear button 
if st.button("Clear"):
    query = ""
    st.rerun()

# Handle code analysis
if btn_click:
    if not query.strip():
        st.warning("Please enter some code to analyze.")
    else:
        with st.spinner("Analyzing your code..."):
            try:
                # Generate response with formatted prompt
                response = model.generate_content(
                    f"Please review this code:\n\n{query}"
                )
                
                # Display response
                if response.text:
                    st.markdown("### Code Review Results")
                    st.markdown(response.text)  # Render markdown
                else:
                    st.error("Received an empty response from the API. Please try again.")
            
            except Exception as e:
                st.error(f"An error occurred while analyzing your code: {str(e)}")
                st.error("Please check your input or try again later.")