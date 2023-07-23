from fastapi import HTTPException

from app.database import Pastes, db
from app.models import Outgoing_Data
from app.routers import router


@router.get("/id/{paste_id}", response_model=Outgoing_Data, status_code=200)
def render_paste(paste_id: str):
    try:
        paste: Pastes = db.query(Pastes).get(paste_id)
        print(f"paste object: {repr(paste)}\npaste object type: {type(paste)}")
        if not paste:
            # FIXME replace this with proper logging
            print(f"WARNING: no results found for '{paste_id}'")
            raise HTTPException(status_code=404, detail="Item not found")
        return paste._to_dict()
    except Exception as e:
        print(f"ERROR: {e}")  # FIXME replace this with proper logging
        raise HTTPException(status_code=500, detail="Internal Server Error")
