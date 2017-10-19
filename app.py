from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from github import Github

from secret import username, password

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:HelloWorld@localhost/helsinki'
db = SQLAlchemy(app)
gh = Github(username, password)

class User(db.Model):
	__tablename__ = 'user'

	username = db.Column(db.String(255), primary_key=True)
	name = db.Column(db.String(255))

	def __init__(self, username, name):
		self.username = username
		self.name = name

class Project(db.Model):
	__tablename__ = 'project'

	uni_name = db.Column(db.String(300), primary_key=True)
	name = db.Column(db.String(255))
	stars = db.Column(db.Integer)
	forks = db.Column(db.Integer)

	def __init__(self, uni_name, name, stars, forks):
		self.uni_name = username
		self.name = name
		self.stars = stars
		self.forks = forks

@app.route('/')
def hello():
	return 'Hello, World'

if __name__ == '__main__':
	app.run()