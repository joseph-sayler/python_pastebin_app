from pydantic import BaseModel


class Updating_Data(BaseModel):
    """Validate incoming data used to update an entry"""

    identifier: str
    title: str
    text: str
