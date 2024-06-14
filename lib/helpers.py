# lib/helpers.py
from models.student import Student
import time
import sys

def helper_1():
    print("Performing useful function#1.")

#TODO Once we finished with story
def exit_program():
    typewriter_effect("Thank you for your story!")
    exit()

def create_student():
    name = typewriter_input("Please, enter your name: ")
    phase = int(typewriter_input("Please, enter your phase:"))
    program = typewriter_input("Please, enter your program:")
    try:
        student = Student.create(name, phase, program)
        print(f"Success: {student}")
    except Exception as exc:
        print("Error", exc)

def typewriter_input(prompt, delay=0.05):
    typewriter_effect(prompt, delay)
    return input()

def typewriter_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 