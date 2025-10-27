import pandas as pd
import sys
from langchain_google_genai import ChatGoogleGenerativeAI
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../source_code')))
import bot_rag as bot_rag
import bot_norag as bot_norag
from transformers import pipeline
import os
os.environ['GOOGLE_API_KEY'] = 'AIzaSyC5OFP8uvEYFlmFEe4PXBTwcluvnUx30cY'
def load_llm_model():
    llm = ChatGoogleGenerativeAI(
        model = 'gemini-2.0-flash',
        temperature = 0,
        max_output_tokens = 10
    )
    return llm

llm = load_llm_model()
data = pd.read_csv('/home/tien/my_project/botchat/test_model/exam_test.csv')

col_exam = data.columns[1: 6]
col_result = data.columns[6]
exams = data[col_exam].apply(lambda x : ''.join([f'{i}: {x[i]}.' for i in col_exam]), axis = 1)
results = data[col_result]

list_path_chunking_test = [(f'vectors_{2**(i + 5)}') for i in range(3, 10)]#[3, 9] 3, 4, 5, 6, 7

for path in list_path_chunking_test:
    count_conrrect = 0
    print(path)
    for i, exam in enumerate(exams):
        print('.', end='')
        if i%10 == 0:
            print(f'\nquestion: {i}')
        bot_result = bot_rag.ai_response(exam, path, llm)
        if str(bot_result).lower() == str(results[i]).lower():
            count_conrrect += 1
    print(f'\nRAG: {path}, conrrect: {count_conrrect}')
print('NoRAG')
for i, exam in enumerate(exams):
    count_conrrect = 0
    bot_result = bot_norag.ai_response(exam, llm)
    if str(bot_result).lower() == str(results[i]).lower():
        count_conrrect += 1
    print('.', end='')
print(f'noRAG conrrect: {count_conrrect}')