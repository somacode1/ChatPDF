import os

from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader



# Large language Model OpenAI API
llm = OpenAI(openai_api_key=os.environ.get('OPENAI_API_KEY'))



#TODO Make this function dynamic use doc url a
def query_pdf(query: str):
    file_name = "How-to-Reset-Migrations.pdf"
    file_path = os.path.join(os.getcwd(), file_name)
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    
    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
    
    docs = faiss_index.similarity_search(query, k=2)
    
    response = ""
    for doc in docs:
        print(str(doc.metadata["page"]) + ":", doc.page_content[:300])

    return response
    





