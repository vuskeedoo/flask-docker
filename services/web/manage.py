from flask.cli import FlaskGroup
from project import app, db, Message

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("test_message")
def seed_db():
    db.session.add(Message(push_id="123abcd4586eddfg"))
    db.session.commit()

if __name__ == "__main__":
    cli()
