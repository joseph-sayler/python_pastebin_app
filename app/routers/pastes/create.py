from secrets import token_urlsafe

from fastapi import HTTPException

from app.database import Pastes, db
from app.models import Incoming_Data
from app.routers import router
from config import Config


@router.post("/paste/", status_code=201)
def recieve_paste(data: Incoming_Data):
    try:
        identifier = token_urlsafe(int(Config.TOKEN_SIZE))
        title = data.title
        paste_text = data.text
        paste: Pastes = Pastes(
            identifier=identifier, paste_text=paste_text, title=title
        )
        db.add(paste)
        db.commit()
        return {"id": identifier}
    except Exception as e:
        print(f"ERROR: {e}")  # FIXME replace this with proper logging
        raise HTTPException(status_code=500, detail="Internal Server Error")
