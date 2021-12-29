from app.routers import router
from app.database import db, Pastes
from fastapi import HTTPException
from pydantic import BaseModel


class Outgoing_Data(BaseModel):
    identifier: str
    title: str
    text: str
    date: str


@router.get("/id/{paste_id}", response_model=Outgoing_Data)
def render_paste(paste_id: str):
    paste = db.query(Pastes).get(paste_id)
    if paste:
        return paste._to_dict()
    else:
        raise HTTPException(status_code=404, detail="Item not found")
