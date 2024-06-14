from models import CONN, CURSOR
from models.student import Student
## TODO import Stories when created

def seed_database():
    Student.drop_table()
    ## TODO add Story drop table
    Student.create_table()
    ## TODO add Story create table

    # Create seed data
    s1 = Student.create("Eliza", 3, "SE")
    # s1.save()
    s2 = Student.create("Alina", 3, "SE")
    # s2.save()
    s3 = Student.create("Angela", 3, "SE")


seed_database()
print("Seeded database")