# Mad Lib!
# Creates a simple story using user input
# learning how to use Tkinter and GUIs

from tkinter import *

class Application(Frame):
    """GUI application which creates a story based on input"""
    def __init__(self, master):
        """Init a frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """creates widgets to get info and display story"""
        Label(self,
              text = "Enter information for a new story"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
              
        # get persons name
        Label(self,
              text = "Person:"
              ).grid(row = 1, column = 0, sticky = W)
        self.person_entry = Entry(self)
        self.person_entry.grid(row = 1, column = 1, sticky = W)
        
        # get persons mood
        Label(self,
              text = "Mood:"
              ).grid(row = 2, column = 0, sticky = W)
              
        # creates variable for single mood
        self.mood = StringVar()
        self.mood.set(None)
        
        # create mood radio buttons
        moods = ["mad", "happy", "confused", "sexually adventurous"]
        col = 1
        for mood in moods:
            Radiobutton(self,
                        text = mood,
                        variable = self.mood,
                        value = mood
                        ).grid(row = 2, column = col, sticky = W)
            col += 1
            
        # create button to fill out text area
        Button(self,
               text = "Click for story",
               command = self.tell_story
               ).grid(row = 3, column = 0, sticky = W)
               
        self.story_text = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_text.grid(row = 4, column = 0, columnspan = 5)
        
    def tell_story(self):
        """gets info from widgets and inserts the finished story"""
        # get values from GUI
        person = self.person_entry.get()
        mood = self.mood.get()
        
        # create the story
        story = "Our loveable champion "
        story += person
        story += " is feeling very "
        story += mood
        story += " today. No one is safe."
        
        # display the story
        self.story_text.delete(0.0, END)
        self.story_text.insert(0.0, story)
        

# main
root = Tk()
root.title("Mad Lib!")
app = Application(root)
root.mainloop()
            