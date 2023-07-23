from datetime import datetime

from fastapi import HTTPException

from app.database import Pastes, db
from app.models import Updating_Data
from app.routers import router


@router.put("/update/", status_code=204)
def update_paste(data: Updating_Data):
    try:
        paste: Pastes = db.query(Pastes).get(data.identifier)
        print(paste)
        if not paste:
            # FIXME replace this with proper logging
            print(f"WARNING: no results found for '{data.identifier}'")
            raise HTTPException(status_code=404, detail="Item not found")
        paste.title = data.title
        paste.paste_text = data.text
        # date changes to represent when change occurred
        # NOTE consider adding a date_changed column and update that instead
        paste.date = datetime.utcnow()
        db.commit()
    except Exception as e:
        print(f"ERROR: {e}")  # FIXME replace this with proper logging
        raise HTTPException(status_code=500, detail="Internal Server Error")
