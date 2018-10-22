from models import *

@app.route("/profesor")
def inicio():
	return render_template('profesor/login.html', val=False)
