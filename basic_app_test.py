from app import start_homunc
from sheet import Character

def test_sample_app():
	

def prepare_sample_table():
	db.drop_all()
	db.create_all()

	tako = Character("Tako Arishi", "Scholar")
	acomo = Character("Acomo Acerai", "Warrior")
	anaravi = Character("Anaravi Revi", "Courtesan")

	db.session.add(tako)
	db.session.add(acomo)
	db.session.add(anaravi)
	db.session.commit()

if __name__ == "__main__":
	test_sample_app()
