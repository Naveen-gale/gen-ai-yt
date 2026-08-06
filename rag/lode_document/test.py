from langchain_community.document_loaders import TextLoader

loader = TextLoader(
    "C:\Users\galen\Desktop\gen ai yt\rag\lode_document\text.txt"
)

documents = loader.load()

print(documents)