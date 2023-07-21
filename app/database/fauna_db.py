from datetime import datetime

from faunadb import query as q
from faunadb.client import FaunaClient

from config import Config


class Fauna_DB:
    """Database class for FaunaDB"""

    _client = None
    _collections = None
    _index = None

    def __init__(self, config=Config):
        self._client = FaunaClient(
            secret=config.FAUNA_SECRET_KEY,
            domain=config.FAUNA_DOMAIN,
            port=443,
            scheme="https",
        )
        self._collections = config.FAUNA_COLLECTION
        self._index = config.FAUNA_INDEX

    def add(self, obj):
        self.__data = obj

    def commit(self):
        # convert to datetime string for storing in fauna
        self.__data.date = datetime.strftime(self.__data.date, "%Y-%m-%d %H:%M:%S.%f")
        # convert __data to dict for storing in fauna
        output = self.__data.__dict__
        self.__client.query(q.create(q.collection(self._collections), {"data": output}))

    def query(self, cls):
        # cls is the fauna db model class used in query
        self.__class = cls
        return self

    def get(self, identifier):
        try:
            results = self._client.query(
                q.get(q.match(q.index(self._index), identifier))
            )
            # convert to datetime object for use in application
            results["data"]["date"] = datetime.strptime(
                results["data"]["date"], "%Y-%m-%d %H:%M:%S.%f"
            )
            results_class = self.__class
            result_obj = results_class()
            result_obj._from_dict(results["data"])
            return result_obj
        except:
            return None
