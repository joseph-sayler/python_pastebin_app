from config import Config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# determines which database to access

if Config.DATABASE_TYPE == "FAUNA":
    from app.database.fauna_db import Fauna_DB
    from app.models import Fauna_Pastes as Pastes
    db = Fauna_DB()
else:  # == "SQLITE"
    from app.models import Base
    from app.models import SQL_Pastes as Pastes
    engine = create_engine(Config.DATABASE_URI)
    Session = sessionmaker()
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    db = Session()