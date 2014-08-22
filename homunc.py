from flask import Flask, url_for, redirect, make_response, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)

@app.route("/")
def hello():
	return "Hello, world!"

@app.route("/characters")
def characters():
	return "Characters here."

@app.route("/characters/<char_name>")
def show_character_sheet(char_name):
	# Check if the character name exists on the database
	queried_character = Character.query.filter_by(character_name=char_name).first_or_404()
	return "Found it!" #render_template("character.html", user=queried_character)

@app.errorhandler(404)
def not_found(error):
	resp = make_response(render_template("whoops.html"), 404)
	resp.headers["X-Something"] = "A value"
	return resp

def start_homunc():
	prepare_table()
	app.run()

def prepare_table():
	db.drop_all()
	db.create_all()

	tako = Character("Tako Arishi", "Scholar")
	acomo = Character("Acomo Acerai", "Warrior")
	anaravi = Character("Anaravi Revi", "Courtesan")

	db.session.add(tako)
	db.session.add(acomo)
	db.session.add(anaravi)
	db.session.commit()

class Character(db.Model):
	c_id = db.Column(db.Integer, primary_key=True)
	character_name = db.Column(db.String(50), unique=False)
	archetype = db.Column(db.String(15), unique=False)

	def __init__(self, name, type):
		self.character_name = name
		self.archetype = type

	def __repr__(self):
		return "<Character: %r>\n" % self.character_name

class CharacterSkills(db.Model):
	s_id = db.Column(db.Integer, primary_key=True)
	awareness = db.Column(db.Integer)
	confidence = db.Column(db.Integer)
	crafting = db.Column(db.Integer)
	finesse = db.Column(db.Integer)
	hardiness = db.Column(db.Integer)
	inspire = db.Column(db.Integer)
	learning = db.Column(db.Integer)
	medicine = db.Column(db.Integer)
	might = db.Column(db.Integer)
	perform = db.Column(db.Integer)
	politics = db.Column(db.Integer)
	ride = db.Column(db.Integer)
	stealth = db.Column(db.Integer)
	survival = db.Column(db.Integer)
	tactics = db.Column(db.Integer)
	wu_wei = db.Column(db.Integer)
	specialties = db.relationship("Specialties", backref="Skills", lazy="dynamic")

	def __init__(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16):
		self.awareness = s1
		self.confidence = s2
		self.crafting = s3
		self.finesse = s4
		self.hardiness = s5
		self.inspire = s6
		self.learning = s7
		self.medicine = s8
		self.might = s9
		self.perform = s10
		self.politics = s11
		self.ride = s12
		self.stealth = s13
		self.survival = s14
		self.tactics = s15
		self.wu_wei = s16
	
class Specialties(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	skill_id = db.Column(db.Integer)
	specialty_name = db.Column(db.String(25))
	# TODO: How do we connect the things..?
		



if __name__ == "__main__":
	start_homunc()
