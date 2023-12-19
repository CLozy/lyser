
import os
from dotenv import load_dotenv

from fastapi import FastAPI


from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()


chat = ChatOpenAI()
chat( [HumanMessage(content = "Translate this sentence from English to Swahili: I love programming")])

# a list of messages 
messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(content="I love programming."),
]
chat(messages)

#wrapping chat model in conversation chain with built-in memory for past user and model inputs
from langchain.chains import ConversationChain

conversation = ConversationChain(llm=chat)
conversation.run("Translate this sentence from English to French:I love programming.")
conversation.run("Translate it to mandarin")

#memory
#simplest and commonly used ConversationBufferMemory , allows storing of messages in buffers, when called in chains it retuns allof the messages it has stored 
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("I love programming.")
memory.chat_memory.add_ai_message("I love programming too.")

#load from memory
memory.load_memory_variables({})

# sliding window of most recent k interactions using ConversationBufferWindowMemory
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=1)

memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})
memory.load_memory_variables({})

