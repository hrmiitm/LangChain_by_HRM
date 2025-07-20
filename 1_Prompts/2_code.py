'''
Prompt Template
Created Date: 21-07-2025

list of sample messages ---> ChatPromptTemplate
dictionary ---> ChatPromptTempate -->
'''

from langchain_core.prompts import ChatPromptTemplate

system_template = "Summarize within {lines}"

my_prompt_template = ChatPromptTemplate([
    ("system", system_template),
    ("user", "write one paragraph on delhi!")
])

prompt = my_prompt_template.invoke({"lines": 1}) # return list of messages

print(prompt)

from langchain.chat_models import init_chat_model

model = init_chat_model(model="gemini-2.0-flash-lite", model_provider="google-genai")

model_result = model.invoke(prompt)
result = model.invoke(prompt)

print(result.content)

