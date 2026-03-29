from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('pdf_file.pdf')

docs = loader.loader()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap=0,
)

chunks = splitter.split_documents(docs)

print(len(chunks))
print(chunks)
