
import os
from dotenv import load_dotenv

from fastapi import FastAPI


from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()


chat = ChatOpenAI()
