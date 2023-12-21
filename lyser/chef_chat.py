
import os
import getpass
from dotenv import load_dotenv

from fastapi import FastAPI


from langchain.chat_models import ChatOpenAI

from langchain.document_loaders import TextLoader, PyPDFLoader, PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import chroma 

from langchain import hub
from langchain.prompts import PromptTemplate, MessagesPlaceholder
from langchain.agents.openai_functions_agent.base import OpenAIFunctionsAgent
from langchain_core.messages import SystemMessage

from langchain.schema import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain.memory import ConversationSummaryMemory

from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.agents.openai_functions_agent.agent_token_buffer_memory import AgentTokenBufferMemory
from langchain.agents import AgentExecutor


load_dotenv()
os.environ["OPENAI_API_KEY"] = getpass.getpass()

#chef chat class
class ChefChat:
    def __init__(self, folder_path, query):
        self.chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        self.folder_path = folder_path
        self.query = query
        self.memory_key="chat_history"

    def data_loader(self):
        #iterate through a folder and load the pdfs in it using pypdfloader
        loader = PyPDFDirectoryLoader(self.folder_path)
        docs = loader.load()
        return docs
    
    def chat_summary(self):
        chat_memory = AgentTokenBufferMemory(llm=self.chat, memory_key=self.memory_key)
        return chat_memory
    
    def format_docs(self):
        docs = self.data_loader()
        return "\n\n".join(doc.page_content for doc in docs)
    
    def rag_pipeline(self):
        #create a rag pipeline
        docs = self.data_loader()

        #text splitting 
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
        splits = text_splitter.split_documents(docs)

        #embedding and storing
        vectorstore = chroma.Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

        # retriever
        retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
        
        #retriever tool
        retriever_tool = create_retriever_tool(retriever, "search recipes", "searches and returns recipes of meals")
        tools = [retriever_tool]

        #custom prompt template 
        system_message = SystemMessage(content="You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Always say 'Happy cooking' at the end of the answer with retrieved recipes.")
        rag_prompt = OpenAIFunctionsAgent.create_prompt(system_message=system_message, extra_prompt_messages=[MessagesPlaceholder(variable_name=self.memory_key)])
        
        #rag agent
        agent = OpenAIFunctionsAgent(llm=self.chat, tools=tools, prompt=rag_prompt)

        #agent constructor
        agent_executor = AgentExecutor(agent=agent, tools=tools, memory=self.chat_summary(), verbose=True, return_intermediate_steps=True)

        agent_result = agent_executor({"input":self.query})

        return agent_result
    
    
 