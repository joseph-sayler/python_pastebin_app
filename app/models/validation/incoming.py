from pydantic import BaseModel


class Incoming_Data(BaseModel):
    """Validate incoming data"""

    title: str
    text: str
