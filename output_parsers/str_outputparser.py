from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

#1st Prompt -> detailed report
template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}'
    input_variable = ['topic']
)

#2nd Prompt -> Summary 
template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text.' /n {text},
    input_variable = ['text']
)

prompt1 = template1.invoke({'topic': 'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result1 = model.invoke(prompt2)

print(result1.content)