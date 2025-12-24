from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt
from langchain_core.runnables import RunnablePassthrough

class AnimeRecommender:
    def __init__(self,retriever,api_key:str,model_name:str):
        self.llm = ChatGroq(api_key=api_key,model=model_name,temperature=0)
        self.prompt = get_anime_prompt()

        # LCEL chain: retrieve documents, pass to prompt, get LLM output
        self.qa_chain = (
            {"context": retriever, "input": RunnablePassthrough()}
            | self.prompt
            | self.llm
        )

    def get_recommendation(self,query:str):
        result = self.qa_chain.invoke(query)
        return result.content