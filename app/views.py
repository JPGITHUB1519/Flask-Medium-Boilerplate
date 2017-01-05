from flask import render_template
from app import app

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

# view
@app.route('/')
@app.route('/index')
def index():
	return "<h1>Hello World</h1>"

@app.route('/welcome')
def welcome():
	return render_template("index.html")

@app.route('/hello/<username>')
def hello(username):
	return render_template("welcome.html", username=username)

@app.route('/users')
def listUsers():
	users = getUsers()
	return render_template('users.html', users=users)

if __name__=='__main__':
	app.run(debug=True)