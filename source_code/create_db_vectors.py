from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

list_path_chunking_test = [(f'vectors_{2**(i + 5)}') for i in range(3, 10)]
pdf_data_path = './raw_data'

def create_db_vector_document(vector_db_path, chunk_size):
    print(f'chunk_size: {chunk_size}, vector_db_path: {vector_db_path}')
    loader = DirectoryLoader(pdf_data_path, glob = '*.pdf', loader_cls = PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = int(chunk_size*0.1),
    )
    chunks = text_splitter.split_documents(documents)
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embedding)
    db.save_local(vector_db_path)
    return db

for i in range(3, 10):
    create_db_vector_document(list_path_chunking_test[i-3], 2**(i+5))