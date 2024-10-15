import random,os
from pics import HANGMANPICS

words=["world","animals","russia"]
word=random.choice(words)
word2=word
word=list(word)
blanks=list(len(word)*"_")

lives=6
guessed=[]

while "_" in blanks and lives:
    os.system("cls" if  os.name=='nt' else "clear")
    print(HANGMANPICS[6-lives])
    print("fill in the blanks:","".join(blanks))
    print(f"You have {lives} attempts left!")
    letter=input("Enter a letter: ")
    if letter in word:
        guessed.append(letter)      
        while letter in word:
            place=word.index(letter)
            blanks[place]=letter
            word[place]="_"          
    else:
        if letter not in guessed:           
            lives-=1
            guessed.append(letter)
        
    
print("The answer is:",word2)

if lives:
    print("You win!")
else:
    print(HANGMANPICS[-1])
    print("You lose!")
