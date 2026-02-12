from fastapi import APIRouter, HTTPException, Depends
from utils.ai_response import get_completion
from schemas.ai_response_schema import AIRequest, AIResponse, ChatHistoryResponse
from repositories.chat_repo import ChatRepo
from db import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.post("/ask", response_model=AIResponse)
def ask_ai(request: AIRequest, db: Session = Depends(get_db)):
    """Get response from AI model and save to history."""
    try:
        response = get_completion(request.message, request.system_prompt)
        # Save to database
        chat_repo = ChatRepo(db)
        chat_repo.save_chat(question=request.message, answer=response)
        return AIResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history", response_model=List[ChatHistoryResponse])
def get_chat_history(db: Session = Depends(get_db)):
    """Get all chat history."""
    chat_repo = ChatRepo(db)
    return chat_repo.get_all_chats()