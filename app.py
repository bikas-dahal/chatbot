from flask import Flask, render_template, request, jsonify
from src.helper import download_hugging_face_embedding, load_pdf
from langchain.prompts import PromptTemplate 
from langchain.chains import RetrievalQA 
from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain_community.vectorstores import Pinecone 
import pinecone 
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_community.llms import CTransformers 
from tqdm.autonotebook import tqdm
from dotenv import load_dotenv
from src.prompt import * 
import os 

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

extracted_data = load_pdf('data/')

embedding = download_hugging_face_embedding() 

# pc = Pinecone(api_key=API_KEY)
# index = pc.Index("chatbot")


# docsearch = Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name='chatbot')

docsearch = Pinecone.from_existing_index('chatbot', embedding)

PROMPT = PromptTemplate(template=Prompt_template, input_variables=['context', 'question'])
chain_type_kwargs = {'prompt': PROMPT}

llm = CTransformers(
    model = 'model/llama-2-7b-chat.bin',
    model_type = 'llama',
    config = {
        'max_new_tokens':512,
        'temperature':0.5,
    }
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',  # Replace with a valid chain type
    retriever=docsearch.as_retriever(search_kwargs={'k':2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

@app.route('/')
def index():
    return render_template('chat.html')


@app.route('/get', methods=['GET', 'POST'])
def chat():
    msg = request.form['msg']
    input = msg
    print(input)
    result = qa({'query':input})
    print('Response: ', result['result'])
    return str(result['result'])



if __name__ == '__main__':
    app.run(debug=True)

