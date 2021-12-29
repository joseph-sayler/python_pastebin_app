from datetime import datetime


class Fauna_Pastes:
    """table to hold user pastes"""

    def __init__(self, identifier=None, title=None, paste_text=None, date=None):
        self.identifier = identifier
        self.title = title
        self.paste_text = paste_text
        self.date = date if date else datetime.utcnow()

    def _from_dict(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def _to_dict(self):
        return {
            "identifier": self.identifier,
            "title": self.title,
            "text": self.paste_text,
            "date": self.date.strftime("%b %d, %Y @ %I:%M %p")
        }

    def __repr__(self):
        return f'<Paste {self.identifier}>'
