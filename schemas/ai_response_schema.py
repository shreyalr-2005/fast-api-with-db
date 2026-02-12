from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AIRequest(BaseModel):
    message: str
    system_prompt: str = "You are a helpful assistant."

class AIResponse(BaseModel):
    response: str

class ChatHistoryResponse(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime

    class Config:
        from_attributes = True
