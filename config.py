from app import app
import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5432/test'#os.environ.get('DATABASE_URL')
app.secret_key = b'1234'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
