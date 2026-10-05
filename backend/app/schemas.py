from pydantic import BaseModel,ConfigDict
from datetime import datetime

class NoteCreate(BaseModel):
    title:str
    content:str
 
 
class NoteUpdate(BaseModel):
    title:str
    content:str    
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    edited_at: datetime | None

    class Config:
        from_attributes = True    