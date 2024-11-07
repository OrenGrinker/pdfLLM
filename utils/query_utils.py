# utils/query_utils.py

from llama_index.llms.openai import OpenAI

def answer_question(index, question, model):
    """Use the index to answer a question."""
    llm = OpenAI(model=model)
    query_engine = index.as_query_engine(llm=llm)
    response = query_engine.query(question)
    return response.response
