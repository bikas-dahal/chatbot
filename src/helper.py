from langchain.prompts import PromptTemplate 
from langchain.chains import RetrievalQA 
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
# from langchain.document_loaders import PyPDFLoader, DirectoryLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_community.llms import CTransformers
from tqdm.autonotebook import tqdm




def load_pdf(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader,
    )

    documents = loader.load()

    return documents


def text_chunks(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )

    chunks = text_splitter.split_documents(data)

    return chunks



def download_hugging_face_embedding():
    embeddings = HuggingFaceEmbeddings(
        # model_name="sentence-transformers/all-mpnet-base-v2",
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        # device="cuda",
    )
    return embeddings