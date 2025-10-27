import pandas as pd
import sys
from langchain_google_genai import ChatGoogleGenerativeAI
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../source_code')))
import bot_rag as bot_rag
import bot_norag as bot_norag
from transformers import pipeline
import os
os.environ['GOOGLE_API_KEY'] = 'AIzaSyCpJHh9CsNlWn7JMurxG9idum-LKJgWoIY'
def load_llm_model():
    llm = ChatGoogleGenerativeAI(
        model = 'gemini-2.0-flash',
        temperature = 0,
        max_output_tokens = 5
    )
    return llm

llm = load_llm_model()

data = pd.read_csv('/home/tien/my_project/botchat/test_model/decision_making_test.csv')
data['Trả lời'] = data['Trả lời'].replace({'Không tiến hành': 'N', 'Tiến hành': 'Y'})
situation = data['Câu hỏi']
results = data['Trả lời']
print(results.value_counts())

list_path_chunking_test = [(f'vectors_{2**(i + 5)}') for i in range(8, 9)]#[3, 9] 3, 4, 5, 6, 7
rag = {
        'Y': 0,
        'N':0,
        'NG':0
    }
norag = {
        'Y': 0,
        'N':0,
        'NG':0
    }

for path in list_path_chunking_test:
    print(path)
    for i, exam in enumerate(situation):
        print('.', end='')
        bot_result = bot_rag.ai_response(exam, path, llm)
        if str(bot_result).upper() == str(results[i]).upper():
            rag[str(bot_result).upper()] += 1
print()
print(rag)
print('NoRAG')
for i, exam in enumerate(situation):
    print('.', end='')
    bot_result = bot_norag.ai_response(exam, llm)
    if str(bot_result).upper() == str(results[i]).upper():
        norag[str(bot_result).upper()] += 1
print()
print(norag)