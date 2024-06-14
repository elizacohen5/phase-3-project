# lib/helpers.py
from models.student import Student

def helper_1():
    print("Performing useful function#1.")

#TODO Once we finished with story
def exit_program():
    print("Thank you for your story!")
    exit()

def create_student():
    name = input("Please, enter your name: ")
    phase = int(input("Please, enter your phase:"))
    program = input("Please, enter your program:")
    try:
        student = Student.create(name, phase, program)
        print(f"Success: {student}")
    except Exception as exc:
        print("Error", exc)
        
