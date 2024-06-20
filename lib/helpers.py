# lib/helpers.py
from models.student import Student
from models.story import Story
import time
import sys

def exit_program():
    typewriter_effect("Thank you for your story!")
    exit()

def create_student():
    name = typewriter_input("Please, enter your name: ").lower()
    phase = int(typewriter_input("Please, enter your phase:"))
    program = typewriter_input("Are you SE or DS Student?")
    try:
        student = Student.create(name, phase, program)
        return student
    except Exception as exc:
        print("Error", exc)

def create_story(student):
    adj1 = typewriter_input("How do you feel on the last Friday of every phase?")
    ridiculous_event = typewriter_input("What is the most absurd thing you've ever witnessed?")
    fictional_villain = typewriter_input("If you had to choose a fictional villain to be your roommate, who would it be?")
    beverage = typewriter_input("If you could have any drink right now, what would it be?")
    emotion = typewriter_input("How are you feeling right now?")
    celebrity = typewriter_input("Who is a celebrity you'd like to take on a date?")
    topic = typewriter_input("What is the most difficult topic so far in bootcamp?")
    animal = typewriter_input("What animal has the most chaotic behavior?")
    stimulant = typewriter_input("On long days, what do you use as a pick-me-up?")
    food = typewriter_input("What food are you craving at this moment?")
    emotional_turmoil = typewriter_input("What emotion best describes going through a significant personal crisis?")
    tech_trend = typewriter_input("What tech trend interests you the most?")
    tv_show = typewriter_input("What is your favorite TV show right now?")
    video_game = typewriter_input("What is the most sadistic video game you have ever played?")
    error = typewriter_input("What is the most annoying error to get while coding?")
    end_of_day_activity = typewriter_input("What is your favorite way to relax after coding all day?")

    
    result =  f"""Welcome to the {adj1} world of the Flatiron School Coding Bootcamp, where every day feels like a {ridiculous_event} orchestrated by 
{fictional_villain}! Each morning starts at 9am, armed with a {beverage} and a {emotion} sense of determination.

You walk into class at 10am sharp, clutching your {beverage} like it’s the Holy Grail. Your instructor, {celebrity}, is already at the board, scribbling 
furiously about {topic} with the energy of a {animal} on {stimulant}.

Lunch rolls around, and you dash out, daydreaming about {food}. You settle down with your {food} and a side of {emotional_turmoil}, while everyone else debates 
{tech_trend} like it’s {tv_show}. Back to the grind. Navigating Canvas is like playing {video_game} where every level is harder than the last. You encounter the 
infamous {error} error. After four hours of unsuccesfully debugging the same error, you give up and go home to drown out your thoughts with {end_of_day_activity}."""
   
    typewriter_effect(result)

    Story.create(student.id, result)

def get_student_by_name():
    typewriter_effect("Please select a name from the following list of students:")
    Student.get_students()
    name = typewriter_input("Please enter a name from the student list: ").lower()
    
    Story.get_student_story(name)

def typewriter_input(prompt, delay=0.05):
    typewriter_effect(prompt, delay)
    return input()

def typewriter_effect(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 