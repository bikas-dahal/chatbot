from pinecone import Pinecone
from dotenv import load_dotenv
import os
from langchain_community.vectorstores import Pinecone
# from langchain.vectorstores import Pinecone as PineconeStore
from langchain_pinecone import PineconeVectorStore
from src.helper import load_pdf, text_chunks, download_hugging_face_embedding
from langchain_community.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os


load_dotenv()


# PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

extracted_data = load_pdf('data/')

text_chunks = text_chunks(extracted_data)

embeddings = download_hugging_face_embedding()


API_KEY = os.getenv("PINECONE_API_KEY")


from pinecone import Pinecone

pc = Pinecone(api_key=API_KEY)
index = pc.Index("chatbot")


docsearch = Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name='chatbot')


# docsearch = Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name='chatbot')