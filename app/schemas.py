from pydantic import BaseModel

class SessionCreate(BaseModel):
    day: str
    subject: str
    topic: str

