from .database import Base
from sqlalchemy import TIMESTAMP, Column, Integer,Boolean,String, text,ForeignKey,Numeric,DateTime
from sqlalchemy import func

class Note(Base):
    __tablename__="notes"
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())
    edited_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    
