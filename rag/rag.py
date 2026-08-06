from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

loder = TextLoader(
    text="C:\Users\galen\Desktop\gen ai yt\rag\lode_document\text.txt"
)
doc = loder.load()

load_dotenv()
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="openai/gpt-oss-20b",
    model_provider="groq",
    temperature=0.7,
)

response = llm.invoke("Explain RAG in simple words.")

print(response.content)