from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def read_vectors_db(vector_db_path):
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(vector_db_path, embedding, allow_dangerous_deserialization=True)
    return db
    
def create_prompt(template):
    prompt = PromptTemplate(template = template, input_variables = ['context','question'])
    return prompt

def create_qa_chain(prompt, llm, db):
    llm_chain = RetrievalQA.from_chain_type(
        llm = llm,
        chain_type = 'stuff',
        retriever = db.as_retriever(search_kwargs = {'k':30}),
        return_source_documents = False,
        chain_type_kwargs = {'prompt':prompt}
    )
    return llm_chain

def ai_response(user_question, vector_db_path, llm):
    template = """
    bạn là chatbot trợ lí y tế, từ kiến thức sau hãy trả lời chính xác câu hỏi sau
    kiến thức: "{context}"
    Câu hỏi: "{question}"
    """
    prompt = create_prompt(template)
    db = read_vectors_db(vector_db_path)
    llm_chain = create_qa_chain(prompt, llm, db)

    question = user_question
    response = llm_chain.invoke({'query': question})
    return response['result']

