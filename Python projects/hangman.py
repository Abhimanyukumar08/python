#...................HANGMAN......................
import random 

def hangman():
    word = random.choice(["python","java","programming","compitetive", "HTML","css","machine learning", "cloud","data science","database"])
    validletters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessword = ""

    while len(word)>0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessword:
                main = main + letter
            else:
                main = main + "_" + " "
        if main==word:
            print(main)
            print("YOU WON")
            break
        
        print("Guess the word: " ,main)
        guess = input()

        if guess in validletters:
            guessword = guessword +guess
        else:
            print("enter a valid letter")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns==9:
                print("yoh have 9 turns left")
                print("---------")
            if turns==8:
                print("yoh have 8 turns left")
                print("---------")
                print("    0     ")
            if turns==7:
                print("yoh have 7 turns left")
                print("---------")
                print("    0     ")
                print("    |     ")
            if turns==6:
                print("yoh have 6 turns left")
                print("---------")
                print("    0     ")
                print("    |     ")
                print("   /      ")
            if turns==5:
                print("yoh have 5 turns left")
                print("---------")
                print("    0     ")
                print("    |     ")
                print("   / \    ")
            if turns==4:
                print("yoh have 4 turns left")
                print("---------")
                print("    0 /   ")
                print("    |     ")
                print("   / \    ")
            if turns==3:
                print("yoh have 3 turns left")
                print("---------")
                print("  \ 0 /   ")
                print("    |     ")
                print("   / \    ")
            if turns==2:
                print("yoh have 2 turns left")
                print("---------")
                print("  \ 0 / | ")
                print("    |     ")
                print("   / \    ")
            if turns==1:
                print("This is the last chance to safe your man")
                print("---------")
                print("  \ 0 /_| ")
                print("    |     ")
                print("   / \    ")
            if turns==0:
                print("YOU LOSE")
                print("---------")
                print("    0 _| ")
                print("   /|\   ")
                print("   / \   ")
            
        
name = input("enter the name: ")

print("Welcome to the game ", name)
print("-------------------------------")
print("You have only 10 attempts to win the game ")
hangman()
print()


