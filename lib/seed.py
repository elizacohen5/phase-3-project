from models import CONN, CURSOR
from models.student import Student
from models.story import Story 

def seed_database():
    Student.drop_table()
    Story.drop_table()
    Student.create_table()
    Story.create_table()

    # Create seed data
    s1 = Student.create("Eliza", 3, "SE")
    # s1.save()
    s2 = Student.create("Alina", 3, "SE")
    # s2.save()
    s3 = Student.create("Angela", 3, "SE")

    story = Story.create(s1, "hi")


seed_database()
print("Seeded database")