from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = " "
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 fact about {topic} \n {format_instruction()}',
    input_variable = ['topic'],
    partial_variable = {'format_instruction': parser.get_format_instructions()}
)


#if we make chain no need to write below lines instead write
#chain = template | model | parser
#result = chain.invoke({'topic': 'black hole'})
#print(result)


prompt = template.invole({'topic': 'black hole'})

result = model.invole(prompt)

final_result = parser.parse(result.content)

print(final_result)