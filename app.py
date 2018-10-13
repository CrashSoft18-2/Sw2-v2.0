from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
db = SQLAlchemy(app)

def init():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    #firebase_admin.initialize_app()

if __name__ == "__main__":
	init()
