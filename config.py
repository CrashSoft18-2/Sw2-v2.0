from app import app
import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://inrbkbfqwjvcnb:83df34940918d53940c4bd30b5a185d3d79726cd36230f4a402f4a8f8579e680@ec2-174-129-35-61.compute-1.amazonaws.com:5432/da8gvk43j45moa'#os.environ.get('DATABASE_URL')
app.secret_key = b'1234'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
