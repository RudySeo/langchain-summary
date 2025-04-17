from pydantic import BaseModel

class SummaryRequest(BaseModel):
    article: str

class SummaryResponse(BaseModel):
    summary: str

class AnalyzeArticleResponse(BaseModel):
    summary: str
    sentiment: str
    category: str