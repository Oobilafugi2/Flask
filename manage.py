from flask.cli import FlaskGroup
from src import app

#  lets us use Flask command line arguments with our app
cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
