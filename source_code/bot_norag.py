from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_google_genai import ChatGoogleGenerativeAI
import re
import os

def ai_response(question: str, llm):
    prompt = f"""bạn là chatbot trợ lí y tế, hãy trả lời chính xác câu hỏi sau
                    Câu hỏi là: {question}"""
    response = llm.invoke(prompt)
    return response.content
