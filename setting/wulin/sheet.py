from app import db

class Character(db.Model):
	c_id = db.Column(db.Integer, primary_key=True)
	character_name = db.Column(db.String(50), unique=False)
	archetype = db.Column(db.String(15), unique=False)

	def __init__(self, name, type):
		self.character_name = name
		self.archetype = type

	def __repr__(self):
		return "<Character: %r>\n" % self.character_name
