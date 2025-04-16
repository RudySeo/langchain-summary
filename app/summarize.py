import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableMap, RunnableSequence

load_dotenv()

# LangChain LLM 구성
llm = ChatOpenAI(
    temperature=0.3,
    model_name="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# 프롬프트 템플릿
prompt = PromptTemplate(
    input_variables=["article"],
    template="""
    다음 기사를 3줄로 요약해줘:

    기사:
    {article}

    요약:
    """
)

# 요약 체인 구성
chain = prompt | llm

# 요약 함수
def summarize_article(article: str) -> str:
  try:
        result = chain.invoke({"article": article})
        return result.content
  except Exception as e:
        print(f"오류확인: {e}")
        return "Error "

