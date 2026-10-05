from fastapi import APIRouter,HTTPException,status,Depends,Response
from .. import schemas,crud
from sqlalchemy.orm import Session
from ..database import get_db

router=APIRouter(prefix="/notes",tags=["Note"])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.NoteResponse)
def create_notes(note:schemas.NoteCreate,db:Session=Depends(get_db)):
    return crud.create_note(db, note)

@router.delete("/{note_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id:int,db:Session=Depends(get_db)):
    deleted=crud.delete_note(db,note_id)
    if not deleted:
        raise HTTPException(status_code=404,detail="Note Not found")
    
@router.put("/{note_id}",status_code=status.HTTP_200_OK,response_model=schemas.NoteResponse)
def edit_note(note_id: int,note:schemas.NoteUpdate,db: Session=Depends(get_db)):
    edit=crud.edit_note(db,note_id,note)
    if not edit:
        raise HTTPException(status_code=404,detail="Note Not found")
    return edit    

@router.get("/",response_model=list[schemas.NoteResponse])
def get_notes(db:Session=Depends(get_db)):
    note=crud.retrieve_note(db)
    return note

@router.get("/{note_id}",response_model=schemas.NoteResponse)
def get_note_id(note_id:int,db:Session=Depends(get_db)):
    note=crud.retrieve_note_id(db,note_id)
    if not note:
        raise HTTPException(status_code=404,detail="Note Not found")
    return note