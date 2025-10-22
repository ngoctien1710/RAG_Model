import gradio as gr
_chat_history = []
_user_question = None
def get_user_question():
    """Trả về câu hỏi người dùng gửi (và reset biến)."""
    global _user_question
    q = _user_question
    _user_question = None
    return q
def send_bot_answer(answer: str):
    """Gửi câu trả lời của bot vào lịch sử chat."""
    global _chat_history
    _chat_history.append((None, answer))
    return _chat_history
def on_user_submit(message, chat_state):
    """Xử lý khi người dùng gửi tin nhắn."""
    global _user_question, _chat_history
    _user_question = message
    if message:
        _chat_history.append((message, None))
    return "", _chat_history
def refresh_chat():
    """Refresh lại khung chat (cập nhật theo biến toàn cục)."""
    global _chat_history
    return _chat_history
def start_ui():
    css = """
    .gradio-container {
        max-width: 1500px;
        margin: auto;
    }
    .chatbot {
        width: 1500px !important;
        height: 700px !important;
        overflow-y: auto;
    }
    """
    with gr.Blocks(css=css) as demo:
        gr.Markdown("## 🩺 Trợ lí y tế")
        chatbot = gr.Chatbot(
            label="Cuộc hội thoại",
            elem_classes=["chatbot"]
        )
        with gr.Row():
            user_input = gr.Textbox(
                placeholder="Nhập tin nhắn...",
                show_label=False,
                scale=5
            )
            send_btn = gr.Button("Gửi", scale=1)
        chat_state = gr.State([])
        send_btn.click(
            on_user_submit,
            [user_input, chat_state],
            [user_input, chatbot]
        )
        user_input.submit(
            on_user_submit,
            [user_input, chat_state],
            [user_input, chatbot]
        )
        timer = gr.Timer(0.5)
        timer.tick(refresh_chat, None, chatbot)
    demo.launch(share=False)
