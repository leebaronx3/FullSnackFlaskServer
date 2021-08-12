import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from mongoengine import connect
from routes.users import users
from routes.projects import projects
from routes.staticData import staticData
from routes.forum import forum
from routes.events import events
from utils.file_uploads_utils import UPLOAD_FOLDER


DB_URI = "mongodb+srv://leebaronx3:lcRNCbPClU0mB7l8@fullsnackmongodb.jbs0p.mongodb.net/fullSnackDB?retryWrites=true&w=majority"
connect(host=DB_URI)

app = Flask(__name__)
CORS(app, supports_credentials=True)


app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(users)
app.register_blueprint(projects)
app.register_blueprint(staticData)
app.register_blueprint(forum)
app.register_blueprint(events)


@app.route('/public/files/<filename>')
@app.route('/projects/download/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=False)


app.run()