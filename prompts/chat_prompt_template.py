from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([    
    (content = 'you are helpful {domain} expert'),
    (content='explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'dusra'})

print(prompt)