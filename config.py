import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    DATABASE_TYPE = os.environ.get('DATABASE_TYPE', None)
    DATABASE_URI = os.environ.get('DATABASE_URI', None)
    FAUNA_SECRET_KEY = os.environ.get("FAUNA_SECRET_KEY", None)
    FAUNA_DOMAIN = os.environ.get("FAUNA_DOMAIN", None)
    FAUNA_COLLECTION = os.environ.get("FAUNA_COLLECTION", None)
    FAUNA_INDEX = os.environ.get("FAUNA_INDEX", None)
    TOKEN_SIZE = os.environ.get("TOKEN_SIZE", 5)
    ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS","http://localhost:8000").split(",")


class Test_config(object):
    DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'tests/data/test_db.db')}"
    TOKEN_SIZE = os.environ.get("TOKEN_SIZE", 5)
