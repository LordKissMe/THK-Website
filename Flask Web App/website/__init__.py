from flask import Flask 

# Flask application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thkfriendsforlifehomiesforever'

    return app