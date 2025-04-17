import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableMap, RunnableSequence
from app.schema import AnalyzeArticleResponse
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
# 프롬프트 감정
sentiment_prompt = PromptTemplate(
    input_variables=["article"],
    template="""
    다음 기사의 감정을 분석하고 긍정적, 부정적 또는 중립적이라고 평가해줘:

    기사:
    {article}

    감정:
    """
)
# 프롬프트 주제 분류
category_prompt = PromptTemplate(
    input_variables=["article"],
    template="""
    다음 기사의 주제를 분류해줘. (정치, 경제, 사회 등)

    기사:
    {article}

    주제:
    """
)

# 요약 체인 구성
chain = prompt | llm
sentiment_chain = sentiment_prompt | llm
category_chain = category_prompt | llm

# 여러 체인을 병렬로 처리하기 위한 RunnableMap
multi_chain = RunnableMap(
    {
        "summary": chain,
        "sentiment": sentiment_chain,
        "category": category_chain,
    }
)


# 요약 함수
def summarize_article(article: str) -> str:
  try:
        result = chain.invoke({"article": article})
        return result.content
  except Exception as e:
        print(f"오류확인: {e}")
        return "Error "


# 멀티 체인 결과 처리 함수
def multi_chain_article(article: str) -> AnalyzeArticleResponse:
    try:
        result = multi_chain.invoke({"article": article})
        
        # 로그로 반환된 결과 확인
        print(f"multi_chain 호출 결과: {result}")

        # 예상된 형식으로 결과 처리
        return AnalyzeArticleResponse(
            summary=result["summary"].content,
            sentiment=result["sentiment"].content,
            category=result["category"].content
        )
    except Exception as e:
        print(f"오류확인: {e}")
        return AnalyzeArticleResponse(summary="Error", sentiment="Error", category="Error")
