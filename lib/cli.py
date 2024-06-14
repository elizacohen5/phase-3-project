# lib/cli.py

from helpers import (
    # exit_program,
    helper_1,
    create_student,
    exit_program,
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        if choice == "1": 
            print("Creating a story")
            create_student()
        if choice == "2":
           print("Getting all stories")
        # else:
        #     print("Invalid input")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a story")
    print("2. Get all stories")
    
    
#     print("Please select an option:")
#     print("0. Exit the program")
#     print(f"""
# Welcome to the [adjective] world of the Flatiron School Coding Bootcamp, where every day feels like a [ridiculous event] networking event orchestrated by a [fictional villain] Targaryen ! Each morning starts at [time] 3pm, armed with [beverage] gin and tonic and a [emotion] depressed sense of determination.

# You walk into class at [time] 7am sharp, clutching your [beverage] earl grey tea like it’s the Holy Grail. Your instructor, [celebrity’s name] Sydney Sweeney, is already at the board, scribbling furiously about [technical topic] Dictionaries. With the energy of a [hyperactive animal] Jaguar on [stimulant] speed, they explain how [programming concept] OOP is just like [getting a cat to fetch].

# Lunch rolls around, and you dash out, daydreaming about [favorite comfort food]. You settle down with your [questionable meal] and a side of [emotional turmoil], while everyone else debates [the next big tech trend] like it’s [a reality TV show]. You try to relax, but your mind keeps wandering back to [unfinished project]. Why does it seem to [have a vendetta] against you?
# Back to the grind. It’s time to tackle [Canvas], the [mysterious] platform that holds all your [assignments]. Navigating Canvas is like playing [a sadistic video game] where every level is harder than the last. You encounter the infamous [“page not loading”] error. Canvas continues to [taunt you] with its [error messages] and [cryptic instructions], but you bravely march on, solving problems like a [determined protagonist] in a [gritty action movie].
# It’s time for coding practice, where you attempt to tame your [rebellious code]. Your project, “[The Impossible App],” is supposed to be a [simple] task, but it morphs into a [nightmare monster] with [bugs] the size of [fictional creatures]. You tackle the [errors] like a [wild-west gunslinger], but they keep [multiplying] like [tribbles in Star Trek]. By [late evening], you’ve written [number] lines of code and deleted [larger number].
# The day ends, and you stagger out like a [zombie] from a [horror movie]. Tomorrow, you’ll battle [React], but tonight you just want to [curl up] with [favorite comfort item] and [forget the world].
# """)


if __name__ == "__main__":
    main()
