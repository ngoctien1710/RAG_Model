from ui import start_ui, get_user_question, send_bot_answer
from bot_norag import ai_response
import threading
from langchain_google_genai import ChatGoogleGenerativeAI
#
import os
os.environ['GOOGLE_API_KEY'] = 'AIzaSyC5OFP8uvEYFlmFEe4PXBTwcluvnUx30cY'
path = '/home/tien/my_project/botchat/vectors'
def load_llm_model():
    llm = ChatGoogleGenerativeAI(
        model = 'gemini-2.0-flash',
        temperature = 0.01,
        max_output_tokens = 2000
    )
    return llm

llm = load_llm_model()

def bot_loop():
    while True:
        q = get_user_question()
        if q:
            answer = ai_response(q, llm)
            send_bot_answer(answer)

if __name__ == "__main__":
    threading.Thread(target=bot_loop, daemon=True).start()  
    start_ui()