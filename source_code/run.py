from ui import start_ui, get_user_question, send_bot_answer
from bot import ai_response
import threading

def bot_loop():
    while True:
        q = get_user_question()
        if q:
            answer = ai_response(q)
            send_bot_answer(answer)

if __name__ == "__main__":
    threading.Thread(target=bot_loop, daemon=True).start()  
    start_ui()