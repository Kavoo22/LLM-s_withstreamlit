from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

## Importing streamlit 
import streamlit as st

import os 
from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
#os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "This is a Chat Bot made to assist you ."),
        ("user", "Question:{question}")
    ]
)

## Streamlit Framework
st.title("ChatBot 3.22")
text_input = st.text_input("Please enter the text that you want to ask .")

## Integrating with the open source LLM 
llm = Ollama(model = "llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if text_input:
    st.write(chain.invoke({"question":text_input}))
