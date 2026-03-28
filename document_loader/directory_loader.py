from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

# docs = loader.lazy_load()

print(docs)
print(len(docs))
print(docs[0])
print(docs[0].page_content)
print(docs[0].metadata)
