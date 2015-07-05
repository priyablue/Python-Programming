# Trivia Challenge
# Trivia game that reads a plain text file

import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    
    points = next_line(the_file)
    if points:
        points = points[0]
        
    explanation = next_line(the_file) 

    return category, question, answers, correct, points, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, points, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(points)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, points, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)
    
    # adds the player and the score to the high_scores list
    if score > 10:
        print("Congratulations, you've earned enough points to go on the High Score board!")
        try:
            high_scores = open("high_scores.txt", "a")
        except IOError as e:
            print("Sorry an error occured, unable to save your score.")
            print("Error:", + e)
            input("Press Enter to exit.")
            sys.exit()
            
        player_high_score = (input("What is your name: ")) + ": " + str(score)
        high_scores.write(player_high_score)
        high_scores.close()
        print("High score added!")
        
        
main()  
input("\n\nPress the enter key to exit.")
