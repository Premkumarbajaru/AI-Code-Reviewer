import streamlit as st
import google.generativeai as ai

# Load API Key securely
GOOGLE_API_KEY = "AIzaSyDzNlNvf7Y_M78xgNMAA2OvXmn4OkCvU4g"  # Replace with your actual API key
api_key = GOOGLE_API_KEY

# Configure API key
ai.configure(api_key=api_key)

# Define system prompt
system_prompt = """You are an AI-powered Code Reviewer.  
Your primary role is to analyze submitted Python code, detect every possible issue, and provide detailed feedback.  

You should:  
1. Identify syntax errors, including indentation issues, missing colons, and incorrect indentation levels.  
2. Detect runtime errors such as undefined variables, type mismatches, and division by zero.  
3. Find logical errors like incorrect conditions, infinite loops, and miscalculations.  
4. Suggest best practices and performance optimizations, including efficient loops, better data structures, and improved readability.  

For each issue:  
- Provide a clear explanation of why it is a problem.  
- Suggest a corrected version of the code with proper indentation, best practices, and efficiency improvements.  
"""

# Initialize the GenerativeModel
model = ai.GenerativeModel(model_name="gemini-1.5-flash")

# Streamlit UI
st.title(":speech_balloon: AI Code Reviewer")
st.write("Paste your Python code below, and the AI will review it for errors and improvements.")

# Text area for user input
query = st.text_area("Enter Your Code Here...", height=300)

# Button to trigger code review
btn_click = st.button("Review Code")

if btn_click and query:
    try:
        # Generate response using the model
        response = model.generate_content(system_prompt + "\n\nCode to Review:\n" + query)
        
        # Display the response
        st.subheader("Code Review Feedback:")
        st.write(response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")
elif btn_click and not query:
    st.warning("Please enter some code to review.")
