from termcolor import colored
import curses as cs

class Text:
    def __init__(self, message, color="white", term=False, curses=False):
        #self.message = colored(message, color)
        self.message = message
        self.color = color
        self.term = term
        self.curses = curses

    def add_message(self, message, color="", space=" "):
        self.message += space + message
        return self
        if color == "":
            color = self.color
        self.message += space + colored(self.message, color)
        return self

    def __str__(self):
        if self.term:
            return self.message
        if self.curses:
            return self.message
        return self.message

    def __repr__(self):
        if self.term:
            return self.message
        if self.curses:
            return self.message
        return self.message
