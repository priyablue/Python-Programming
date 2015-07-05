# A simple Guess My Number game with a GUI

import random
from tkinter import *

class Application(Frame):
    """GUI Application which lets a user play Guess My Number"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.reset_game()
        
    def create_widgets(self):
        """Creates widgets to play Guess My Number"""
        
        # get users guess
        Label(self,
              text = "Guess:"
              ).grid(row = 0, column = 0, sticky = W)
        self.user_guess = Entry(self)
        self.user_guess.grid(row = 0, column = 1, sticky = W)
        
        # submit guess
        Button(self,
               text = "Submit",
               command = self.submit
               ).grid(row = 1, column = 0, sticky = W)
               
        # reset game
        Button(self,
               text = "Reset",
               command = self.reset_game
               ).grid(row = 2, column = 0, sticky= W)
               
        # set difficulty
        self.difficulty = StringVar()
        self.difficulty.set(100)
        
        # creat radio buttons to change difficulty
        Radiobutton(self,
                    text = "1-10",
                    variable = self.difficulty,
                    value = 10
                    ).grid(row = 2, column = 1, sticky = W)
                    
        Radiobutton(self,
                    text = "1-100",
                    variable = self.difficulty,
                    value = 100
                    ).grid(row = 2, column = 1, sticky = E)
               
        # text display area
        self.display = Text(self, width = 50, height = 10, wrap = WORD)
        self.display.grid(row = 4, column = 0, columnspan = 2)
              
        
    def reset_game(self):
        """Resets the game"""
        self.comp_num = random.randint(1,int(self.difficulty.get()))
        self.guesses = 5
        self.display.delete(0.0, END)
        self.display.insert(0.0, "I have picked a number between 1-{}".format(self.difficulty.get()))
        self.display.insert(0.0, "You have {} guesses.\n".format(self.guesses))
        
    def update_display(self, high_low):
        """Updates display"""
        if self.guesses == 1:
            self.display.insert(0.0, "You have {} guess left\n" \
                                "{} than {}.\n".format(self.guesses, high_low, self.user_input))
        elif self.guesses == 0:
            self.display.insert(0.0, "You lose, my number was {}.\n".format(self.comp_num))
        else:
            self.display.insert(0.0, "You have {} guesses left\n" \
                                "{} than {}.\n".format(self.guesses, high_low, self.user_input))
        
        
    def submit(self):
        """Checks user input against computers number"""
        if self.guesses:
            try:
                self.user_input = int(self.user_guess.get())
                
                # if number, check against computer
                if self.user_input > int(self.difficulty.get()) or \
                   self.user_input < 0:
                   self.display.insert(0.0, "Out of range.\n")
                   
                elif self.user_input > self.comp_num:
                    self.guesses -= 1
                    self.update_display("Lower")
                    
                elif self.user_input < self.comp_num:
                    self.guesses -= 1
                    self.update_display("Higher")
                    
                else:
                    self.display.insert(0.0, "***BINGO***\n")
                    
            except ValueError:
                self.display.insert(0.0, "Please enter a number\n")
        else:
            self.display.insert(0.0, "Sorry you have ran out of guesses\n"\
                                     "Please reset the game to have another go.\n")
            
            
            
            
root = Tk()
root.title("Guess My Number")
app = Application(root)
root.mainloop()