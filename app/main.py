from fastapi import FastAPI
from app.schema import SummaryRequest, SummaryResponse,AnalyzeArticleResponse
from app.summarize import summarize_article,multi_chain_article

app = FastAPI(title="LangChain Summary API")

@app.post("/summary", response_model=SummaryResponse)
def summarize(req: SummaryRequest):
    result = summarize_article(req.article)
    return SummaryResponse(summary=result)


# 첫 번째 API: 멀티 체인 실행 (요약, 감정 분석, 카테고리 분류)
@app.post("/analyze_article", response_model=AnalyzeArticleResponse)
def analyze_article(req: SummaryRequest):
    return multi_chain_article(req.article)