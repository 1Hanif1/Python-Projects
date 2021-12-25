# Madlib generator using python and tkinter module for GUI
from tkinter import *


class Madlib():
    def __init__(self):
        print("Welcome to Madlibs generator :)\nClick on any madlib and start writing words on the command line! Have fun :)")

        self.load_interface()

    def load_interface(self):
        window = Tk()
        window.title("Madlibs Generator")
        Label(window, text="Madlibs generator").pack()
        Button(window, text="Hello Kitty", padx=30,
               pady=20, width=30, command=self.hello_kitty).pack()
        Button(window, text="Day in a life of a teacher", padx=30,
               pady=20, width=30, command=self.day_in_a_life_of_a_teacher).pack()
        Button(window, text="A letter from George", padx=30,
               pady=20, width=30, command=self.day_in_a_life_of_a_teacher).pack()
        window.mainloop()

    def display_story(self, story):
        for line in story:
            print(line)

    def day_in_a_life_of_a_teacher(self):
        story = [
            f"6:00 A.M: Wake up to the sound of the {input('noun: ')} beeping. {input('verb: ')} out of bed and go immediately to the {input('type of liquid: ')} maker. Ahhhh... much better!",
            f"7:30 A.M: Walk the {input('Animal: ')}, eat {input('any food: ')} for breakfast, and drive to school while listening to \"{input('song name: ')}\" on the radio",
            f"9:00 A.M: First Period! Teach {input('Subject: ')}, hand back pop {input('noun: ')}, answer questions about how to get extra credit",
            f"12:00 P.M: Only {input('Number: ')} minutes for lunch! Eat left over {input('Type of food: ')} as quickly as possible. And drink another cup of {input('Type of liquid: ')} of course!",
            f"3:00 P.M: School day is over for the {input('Plural Noun: ')}, but the {input('Adjective: ')} work has just begun. Grade {input('Plural Noun: ')}, write assignments, hang {input('Adjective: ')} decorations in classroom.",
            f"5:00 P.M: Drive Home, heat up {input('Type of food: ')} for dinner in the microwave, fall asleep while watching \" The Real {input('Plural Noun: ')} of (the) {input('A Place: ')} \" on television! "
        ]
        self.display_story(story)

    def hello_kitty(self):
        story = [
            f"Hello Kitty loves her {input('Adjective: ')} family.",
            f"Her twin, Mimmy, is also her best {input('Noun: ')} in the whole wide {input('Noun: ')}.",
            f"She looks just like Hello Kitty, except she wears a yellow bow on her right {input('Part of body: ')}.",
            f"Hello Kitty's {input('Adjective: ')} parents are her mama, Mary and her papa, George.",
            f"Mama is kind and {input('Adjective: ')} {input('Noun: ')}.",
            f"She loves to cook and take care of {input('Plural Noun: ')}.",
            f"Papa is always making {input('Adjective: ')} jokes.",
            f"He is a hard working {input('Noun: ')} and a/an {input('Adjective: ')} papa to Hello Kitty and Mimmy.",
            f"Hello Kitty's grandma and grandpa are named Margaret and Anthony. Grandpa loves to paint {input('Plural Noun: ')}.",
            f"Grandma enjoys making {input('Plural noun: ')} for hello kitty and Mimmy, and she likes to embroider {input('Plural noun: ')}.",
            f"Hello Kitty's family is a very {input('Adjective: ')} part of her {input('Noun: ')}"
        ]
        self.display_story(story)

    def a_letter_from_george(self):
        story = [
            f"Hello, my fellow {input('Plural noun: ')} in 2020, it's me george washington, the first {input('Occupation: ')}.",
            f"I am writing from (the) {input('A place: ')}, where I have been living secretly for the past {input('Number: ')} years.",
            f"I am concerned by the {input('Adjective: ')} state of affairs in America these days.",
            f"It seems that your politicians are more concerned with {input('-ing verb: ')} each other than with listening to the {input('Plural noun: ')} of the people.",
            f"When we declared our independence from (the) {input('A place: ')}, we set forth on a/an {input('Adjective: ')} path guided by the voices of the everyday {input('Plural noun: ')}.",
            f"If we're going to keep {input('-ing verb: ')}, then we need to learn how to respect all {input('Plural noun: ')}.",
            f"Don't get me wrong we had {input('Adjective: ')} problems in my day too.",
            f"Benjamin Franklin once called me a/an {input('Noun: ')} and kicked me in the {input('Part of the body: ')}.",
            f"But in the end of the day we were able to {input('verb: ')} in harmony.",
            f"Let us find that {input('Adjective: ')} spirit once again, or else i'm taking my {input('Part of the body')} off the quarter!"
        ]
        self.display_story(story)


if __name__ == '__main__':
    Madlib()
