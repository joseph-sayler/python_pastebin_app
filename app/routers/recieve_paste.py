from app.routers import router
from app.database import db, Pastes
from fastapi import HTTPException
from pydantic import BaseModel
from secrets import token_urlsafe
from config import Database_config as config


class Incoming_Data(BaseModel):
    title: str
    text: str


@router.post("/paste/")
def recieve_paste(data: Incoming_Data):
    try:
        identifier = token_urlsafe(int(config.TOKEN_SIZE))
        title = data.title
        paste_text = data.text
        paste = Pastes(identifier=identifier,
                       paste_text=paste_text, title=title)
        db.add(paste)
        db.commit()
        return {"id": identifier}
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
