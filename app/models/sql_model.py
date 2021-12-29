from datetime import datetime
from config import Config
from sqlalchemy import Column, Text, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SQL_Pastes(Base):
    """table to hold user pastes"""

    __tablename__ = "pastes"

    identifier = Column(String(Config.TOKEN_SIZE), nullable=False,
                        unique=True, primary_key=True)
    title = Column(Text, nullable=False)
    paste_text = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow())

    def _to_dict(self):
        return {
            "identifier": self.identifier,
            "title": self.title,
            "text": self.paste_text,
            "date": self.date.strftime("%b %d, %Y @ %I:%M %p")
        }

    def __repr__(self):
        return f'<Paste {self.identifier}>'
