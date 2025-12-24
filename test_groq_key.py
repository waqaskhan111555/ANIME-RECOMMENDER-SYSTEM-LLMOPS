#!/usr/bin/env python
"""Test script to validate Groq API key."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("❌ GROQ_API_KEY not found in .env file")
    exit(1)

print(f"Testing API key: {GROQ_API_KEY[:20]}...{GROQ_API_KEY[-10:]}")
print()

try:
    from langchain_groq import ChatGroq
    
    # Initialize Groq model
    llm = ChatGroq(
        model="mixtral-8x7b-32768",
        temperature=0,
        api_key=GROQ_API_KEY
    )
    
    # Test with a simple prompt
    print("Sending test request to Groq API...")
    response = llm.invoke("What is 2+2?")
    
    print("✅ API Key is VALID!")
    print(f"Response: {response.content}")
    
except Exception as e:
    print(f"❌ API Key is INVALID or ERROR occurred:")
    print(f"Error: {str(e)}")
    exit(1)
