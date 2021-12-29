# Pastebin clone in Python

This is a demo app showing my skills in using [FastAPI](https://fastapi.tiangolo.com/), [ORMs](https://www.sqlalchemy.org/), databases, [unit testing](https://docs.pytest.org), software documentation, and devops related skills like setting up an online web server, accessing a database via API, setting up CI/CD pipelines, etc.

The plan is to develop this locally, using sqlite as the db. Then host this on [Heroku](https://www.heroku.com/) and use an online, serverless database ([Fauna](https://fauna.com/)) to hold all the data. In the process I plan on creating a CI/CD pipeline for unit testing and Heroku deployment.

This is actually a [reimplementation](https://github.com/joseph-sayler/python_pastebin_app_old) of a Flask version I wrote a few months ago, but this time I used FastAPI to generate a REST API. It has most of the same parts as the original, but now the front end is separate from the API, SQLAlchemy is used instead of Flask-SQLAlchemy, and a few parts of the custom FaunaDB adapter class have been removed to allow for compatibility with FastAPI.

Also, [poetry](https://python-poetry.org/docs/) is used for python dependency management. And a JavaScript framework will be used for the front end.

## ToDo
- [ ] develop front end (vue? react?)
- [ ] set up CI/CD pipeline to run current unit tests after each push
- [ ] deploy to heroku
