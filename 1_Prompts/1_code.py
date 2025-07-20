'''
Basic Input Output & History Chatbot
Date: 21-07-2025

init_chat_model OBJECT ==> take model and model_provider
ItsObjet has ==> invoke method  ==> return ai messages

[systemmessage, humanmessage, ....] ---> obj.invoke(..) ---> aimessage
[systemmessage, humanmessage, ....] ---> obj.stream(..) ---> generator having aimessageChunk list

'''


# pip install langchain
# pip install -qU "langchain[google-genai]"


import getpass # getpass is used to securely prompt for and input sensitive information
import os
from pprint import pprint

if not os.getenv("GOOGLE_API_KEY"):
    print("GOOGLE_API_KEY is not set yet!!! Hence you need to enter it")
    os.environ['GOOGLE_API_KEY'] = getpass.getpass("Enter Gemini API Key: ")

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

model = init_chat_model(model="gemini-2.0-flash-lite", model_provider="google-genai")

#  ChatModels are instances of LangChain Runnables
#  ChatModels receive message objects as input and generate message objects as output. 

messages = [
    SystemMessage("Modify in comedy way!"),
    HumanMessage("How are You?")
]

### Way1
# result = model.invoke(messages)
# print(type(result), result, sep='\n') # <class 'langchain_core.messages.ai.AIMessage'>

### Way2
# for token in model.stream(messages):
#     print(token.content, end='', flush=True)

### Way3
result1 = model.invoke(messages)
messages.append(result1)

messages.append(HumanMessage("What i just prompt to yo?"))
result2 = model.invoke(messages)
messages.append(result2)

pprint(messages)
