# lib/cli.py

from helpers import (
    create_student,
    exit_program,
    create_story,
    get_student_by_name
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1": 
            print("Creating a story")
            student = create_student()
            create_story(student)
        elif choice == "2":
           print("Get story by student name")
           get_student_by_name()
        else:
            print("Invalid input")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a story")
    print("2. Get story by student name")


if __name__ == "__main__":
    main()
