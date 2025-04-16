from fastapi import FastAPI
from app.schema import SummaryRequest, SummaryResponse
from app.summarize import summarize_article

app = FastAPI(title="LangChain Summary API")

@app.post("/summary", response_model=SummaryResponse)
def summarize(req: SummaryRequest):
    result = summarize_article(req.article)
    return SummaryResponse(summary=result)
