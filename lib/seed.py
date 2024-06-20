from models import CONN, CURSOR
from models.student import Student
from models.story import Story

def seed_database():
    Student.drop_table()
    Story.drop_table()
    Student.create_table()
    Story.create_table()

    # Create seed data
    s1 = Student.create("eliza", 3, "SE")
    s2 = Student.create("alina", 3, "SE")
    s3 = Student.create("angela", 3, "SE")

    story1 = Story.create(s1.id, """Welcome to the happy world of the Flatiron School Coding Bootcamp, where every day feels like a networking event orchestrated by 
Targaryen!""")
    story2 = Story.create(s2.id, """Welcome to the sad world of the Flatiron School Coding Bootcamp, where every day feels like a sleepover orchestrated by 
The White Walker!""")
    story3 = Story.create(s3.id, """Welcome to the exciting world of the Flatiron School Coding Bootcamp, where every day feels like a marathon orchestrated by 
Lannister!""")


seed_database()
print("Seeded database")