from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json, requests
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.config.from_object("project.config.Config") # Postgres
db = SQLAlchemy(app)

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    push_id = db.Column(db.String(100), unique=True, nullable=False)
    inbound_id = db.Column(db.String(100), unique=True, nullable=True)
    subscription_id = db.Column(db.String(50), unique=False, nullable=True)
    phone_number = db.Column(db.String(15), unique=False, nullable=True)
    keyword = db.Column(db.String(50), unique=False, nullable=True)
    contents = db.Column(db.String(160), unique=False, nullable=True)

    def __init__(self, push_id):
        self.push_id = push_id

@app.route('/', methods=['GET'])
def index():
    return('OK')

# /inbound will retrieve GET and POST requests
@app.route('/inbound', methods=['GET', 'POST'])
def inbound():
    # Listener for Trumpia inbound messages
    # http://classic.trumpia.com/api/inbound-push.php
    if request.method == 'GET':
        # Return 200 OK if empty GET is sent
        if 'xml' not in request.args:
            return('200 YES')
        else:
            response = request.args['xml']
            # Save XML in string
            root = ET.fromstring(response)
            for child in root:
                # Saving child tag and values to variable
                push_id_tag,push_id = child.tag,child.text
                # Print
                print (str(push_id_tag)+": "+str(push_id))
            return ('Received')
        return ('Received')

    # POST Method for JSON PUSH Notifications
    if request.method == 'POST':
        response = request.get_json()
        print(response)
        return ('Received')
    return ('Received')

if __name__ == "__main__":
    app.run()
