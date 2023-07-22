from fastapi import HTTPException

from app.database import Pastes, db
from app.models import Outgoing_Data
from app.routers import router


@router.get("/id/{paste_id}", response_model=Outgoing_Data)
def render_paste(paste_id: str):
    paste = db.query(Pastes).get(paste_id)
    if paste:
        return paste._to_dict()
    else:
        raise HTTPException(status_code=404, detail="Item not found")
