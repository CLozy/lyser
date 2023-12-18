import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key)

#building with langchain
#langchain expression language (LCEL) is a langchain way of composing of modules used to build language applications
