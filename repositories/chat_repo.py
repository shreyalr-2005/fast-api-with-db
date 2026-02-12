from models import ChatHistory
from sqlalchemy.orm import Session

class ChatRepo:
    def __init__(self, db: Session):
        self.db = db

    def save_chat(self, question: str, answer: str):
        chat = ChatHistory(question=question, answer=answer)
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)
        return chat

    def get_all_chats(self):
        return self.db.query(ChatHistory).order_by(ChatHistory.created_at.desc()).all()
