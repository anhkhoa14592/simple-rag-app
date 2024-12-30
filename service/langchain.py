from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os

from model.request_scheme import LLMOutput


# Khai báo chain bằng LCELs

def generate_chain():
    gemini_model = "gemini-1.5-flash"

    llm = ChatGoogleGenerativeAI(
        google_api_key=os.getenv('GEMINI_API'),
        model=gemini_model,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
    )

    parser = JsonOutputParser(pydantic_object=LLMOutput)

    prompt_template = PromptTemplate.from_template(
        template="Answer the question from question {question}. The following are some information you can learn:{rag}\n.\n{output_instruction}\nYou HAVE TO answer in Vietnamese.",
        input=["question", "rag"],
        partial_variables={"output_instruction": parser.get_format_instructions()},
    )
    chain = prompt_template | llm | parser

    return chain
