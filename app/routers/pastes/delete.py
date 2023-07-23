from fastapi import HTTPException

from app.database import Pastes, db
from app.routers import router


@router.delete("/delete/{paste_id}", status_code=204)
def remove_paste(paste_id: str):
    try:
        paste: Pastes = db.query(Pastes).get(paste_id)
        if not paste:
            # FIXME replace this with proper logging
            print(f"WARNING: no results found for '{paste_id}'")
            raise HTTPException(status_code=404, detail="Item not found")
        db.delete(paste)
        db.commit()
    except Exception as e:
        print(f"ERROR: {e}")  # FIXME replace this with proper logging
        raise HTTPException(status_code=500, detail="Internal Server Error")
