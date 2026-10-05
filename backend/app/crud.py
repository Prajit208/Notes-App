from sqlalchemy.orm import Session
from . import models,schemas

def create_note(db:Session,note:schemas.NoteCreate):
    new_note=models.Note(title=note.title,content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

def delete_note(db:Session,note_id:int):
    note=db.query(models.Note).filter(models.Note.id ==note_id).first()
    if note is None:
        return False
    db.delete(note)
    db.commit()
    return True

def edit_note(db:Session,note_id: int,note:schemas.NoteUpdate):
    get_note=db.query(models.Note).filter(models.Note.id==note_id).first()
    if get_note is None:
        return None

    get_note.title=note.title
    get_note.content=note.content
    db.commit()
    db.refresh(get_note)
    return get_note
    
def retrieve_note(db:Session):
    note=db.query(models.Note).all()
    if note is None:
        return None    
    return note

def retrieve_note_id(db:Session,note_id:int):
    note=db.query(models.Note).filter(models.Note.id==note_id).first()
    if note is None:
        return None
    return note