from pydantic import BaseModel

class userSchema(BaseModel):
    email: str
    password: str