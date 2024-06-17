# lib/helpers.py
from models.student import Student
from models.story import Story
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
    program = typewriter_input("Are you SE or DS Student?")
    try:
        student = Student.create(name, phase, program)
        print(f"Success: {student}")
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
    emotional_turmoil = typewriter_input("How would you describe the feeling of going through a significant personal crisis?")
    tech_trend = typewriter_input("What tech trend interests you the most?")
    tv_show = typewriter_input("What is your favorite TV show right now?")
    video_game = typewriter_input("What is the most sadistic video game you have ever played?")
    error = typewriter_input("What is the most annoying error to get while coding?")
    end_of_day_activity = typewriter_input("What is your favorite way to relax after coding all day?")
    # try: 
        # story = Story.create(student, result)
        # print(story)
    # except Exception as exc:
    #     print("Error", exc)
    result = f"""Welcome to the {adj1} world of the Flatiron School Coding Bootcamp, where every day feels like a {ridiculous_event} orchestrated by a {fictional_villain}! Each morning starts at 9am, armed with {beverage} and a {emotion} sense of determination.

You walk into class at [time] 7am sharp, clutching your [beverage] earl grey tea like it’s the Holy Grail. Your instructor, [celebrity’s name] Sydney Sweeney, is already at the board, scribbling furiously about [technical topic] Dictionaries. With the energy of a [hyperactive animal] Jaguar on [stimulant] speed, they explain how [programming concept] OOP is just like [getting a cat to fetch].

Lunch rolls around, and you dash out, daydreaming about [favorite comfort food]. You settle down with your [questionable meal] and a side of [emotional turmoil], while everyone else debates [the next big tech trend] like it’s [a reality TV show]. You try to relax, but your mind keeps wandering back to [unfinished project]. Why does it seem to [have a vendetta] against you?
Back to the grind. It’s time to tackle [Canvas], the [mysterious] platform that holds all your [assignments]. Navigating Canvas is like playing [a sadistic video game] where every level is harder than the last. You encounter the infamous [“page not loading”] error. Canvas continues to [taunt you] with its [error messages] and [cryptic instructions], but you bravely march on, solving problems like a [determined protagonist] in a [gritty action movie].
It’s time for coding practice, where you attempt to tame your [rebellious code]. Your project, “[The Impossible App],” is supposed to be a [simple] task, but it morphs into a [nightmare monster] with [bugs] the size of [fictional creatures]. You tackle the [errors] like a [wild-west gunslinger], but they keep [multiplying] like [tribbles in Star Trek]. By [late evening], you’ve written [number] lines of code and deleted [larger number].
The day ends, and you stagger out like a [zombie] from a [horror movie]. Tomorrow, you’ll battle [React], but tonight you just want to [curl up] with [favorite comfort item] and [forget the world]."""

    typewriter_effect(result)

    Story.create(student, result)


def typewriter_input(prompt, delay=0.05):
    typewriter_effect(prompt, delay)
    return input()

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 