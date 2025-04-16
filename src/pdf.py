from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_chunks_from_pdf(file):
    loader = PyPDFLoader(file)
    pages = loader.load()

    # define a splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    # split each page into smaller chunks
    chunks = splitter.split_documents(pages)
    return chunks