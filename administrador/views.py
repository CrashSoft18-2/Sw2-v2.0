from utils import *
from models import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime

@app.route("/administrador")
def administradorUC():
	return render_template('temp/temp.html')
