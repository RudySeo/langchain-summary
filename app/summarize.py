import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

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
chain = LLMChain(llm=llm, prompt=prompt)

# 요약 함수
def summarize_article(article: str) -> str:
    return chain.run(article=article)




{
  "summary": "2025년 1분기 삼성전자 실적 발표, 연결 기준 매출 76조 원, 영업이익 6조 4천억 원 기록.\\n전년 대비 매출 12%, 영업이익 57% 증가로 반도체 부문 회복과 프리미엄 스마트폰 판매 호조로 실적 향상.\\n인공지능 반도체와 차세대 메모리 기술 개발에 집중 투자로 향후 성장 가능성에 대한 기대 모음."
}