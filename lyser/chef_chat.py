
import os
import getpass
from dotenv import load_dotenv

from fastapi import FastAPI


from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.document_loaders import TextLoader, PyPDFLoader


load_dotenv()
os.environ["OPENAI_API_KEY"] = getpass.getpass()

chat = ChatOpenAI()


