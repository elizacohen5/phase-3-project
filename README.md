# Mad Libs for Flatiron

This is a CLI app that generates a Mad Lib type story for students at the Flatiron school in a creative and interactive way. Users are able to create and save stories to a database using an ORM, and find stories by user name. 

---

## Models
Sqlite3 is used to initialize and connect the sqlite database with Pythong objects. Two classes were stored in a relational database to enable interactivity:
    1. Student - When creating a story, users were prompted to enter information (student name, phase, program) by the CLI. User entries were validated and used to create instances of the Student class. Student instances were also stored in the database within the students table, along with a primary key.
    2. Stories - When creating a story, users were prompted by creative questions by the CLI. The user entries were used to generate a Mad Lib style story based on the experience of a student in a Flatiron bootcamp. Once completed, the story was saved to the stories table in the database, along with a generated primary key, and foreign key linking the story to the student id. 

## CLI 
This app runs on the CLI in Terminal. Once run, the user is first shown a list of menu items, allowing them to select from the following list. Helper functions are executed upon user selection after the main menu.
    0. Exit the program
        1. exit_program: Closes the program using the exit() function
    1. Create a story
        1. create_student: Prompts a user to enter name, phase, and program, creates an instance of Student, stores it to the students table, and returns the Student instance.
        2. create_story: Takes in the parameter of the Student instance created, prompts user to answer questions, creates a Story instance based on user inputs and Student parameter, stores it to the stories table, and prints the new story.
    2. Find story by student name
        1. get_student_by_name: Displays a list of student names stored in the students table.
        2. Prompts the user the enter the student name based on the list provided
        3. get_student_story: Takes the user inputted student name and finds associated student story using a join table to correlate the primary key 'id' in the students table to the foreign key 'student_id' in the story table. The story is then printed.

Custom typewriter_input and typewriter_effect functions were developed to print and prompt users on the CLI. The effect takes in the text to be dispalyed and adds a time delay between printing each character in the text.
