from pydantic import BaseModel


class Outgoing_Data(BaseModel):
    """Validate data being sent to client has these properties"""

    identifier: str
    title: str
    text: str
    date: str
