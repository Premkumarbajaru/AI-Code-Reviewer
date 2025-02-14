import streamlit as st
import google.generativeai as ai

# Load API Key securely
api_key = st.secrets["GOOGLE_API_KEY"]

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

# ✅ FIX: Proper way to define the GenerativeModel
model = ai.GenerativeModel(model_name="gemini-1.5-flash")  # Fix here

# Streamlit UI
st.title(":speech_balloon: AI Code Reviewer")
query = st.text_area("Enter Your Code Here...")
btn_click = st.button("Generate")

if btn_click:
    response = model.generate_content(query)  # Generate response
    st.write(response.text)
