#!/bin/bash

# note! ensure a .env file exists with a minimum of the following:
# DATABASE_TYPE="SQLITE"
# DATABASE_URI="sqlite:///tests/data/test_db.db"

uvicorn app.app:app