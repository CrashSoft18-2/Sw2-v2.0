from flask import Flask
import config
import views
import os

app = Flask(__name__)

def init():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    #firebase_admin.initialize_app()

if __name__ == "__main__":
	init()
