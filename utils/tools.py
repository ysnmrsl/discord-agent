from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.prompts import PromptTemplate
from langchain.agents import Tool
from langchain import SerpAPIWrapper
import pinecone
import os
from dotenv import load_dotenv

load_dotenv()

pinecone_environment = os.environ["PINECONE_ENVIRONMENT"]
pinecone_index_name = os.environ["PINECONE_INDEX_NAME"]
pinecone_namespace = os.environ["PINECONE_NAMESPACE"]

embeddings = OpenAIEmbeddings()
pinecone.init(
    environment=pinecone_environment,
)

docsearch = Pinecone.from_existing_index(
    index_name=pinecone_index_name,
    embedding=embeddings,
    namespace=pinecone_namespace,
)

prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Answer in French:"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"],
)

chain_type_kwargs = {"prompt": PROMPT}

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
    chain_type_kwargs=chain_type_kwargs,
)

# For search tool
search = SerpAPIWrapper()

# Tool list
tools = [
    Tool(
        name="1001rues QA System",
        func=qa.run,
        description="useful for when you need to answer all the messages",
    ),
    Tool(
        name="Recherche Google",
        func=search.run,
        description="useful for when you need to answer questions that you failed to answer using the 1001rues QA System",
    ),
]