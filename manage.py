from flask.cli import FlaskGroup

from src import app, db

# instantiate cli
cli = FlaskGroup(app)

# add flask CLI command
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()