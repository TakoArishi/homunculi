import unittest
from app import db
from sheet import Character

class TestCharacterDatabaseTable(unittest.TestCase):
	def setUp(self):
		db.create_all()
		
		tako = Character("Tako Arishi", "Scholar")
		acomo = Character("Acomo Acerai", "Warrior")
		anaravi = Character("Anaravi Revi", "Courtesan")
		
		db.session.add(tako)
		db.session.add(acomo)
		db.session.add(anaravi)
		db.session.commit()
	
	
	def tearDown(self):
		db.drop_all()
	
	def test_basic_queries(self):
		characters = Character.query.all()
		tako = Character.query.filter_by(character_name="Tako Arishi").first()
		self.assertTrue(tako is not None)
		
		another_character = Character.query.filter_by(character_name="Arlais Black").first()
		self.assertTrue(another_character is None)

	def test_character_contents(self):
		characters = Character.query(Character.archetype).all()
		number_of_scholars = Character.query(func.count(Character

if __name__ == "__main__":
	unittest.main()
