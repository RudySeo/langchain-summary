from pydantic import BaseModel

class SummaryRequest(BaseModel):
    article: str

class SummaryResponse(BaseModel):
    summary: str
