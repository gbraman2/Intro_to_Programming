Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # This is a header for the application
... # You should read this header and insert your name and your date below as part of the peer review
... # This is a typical part of any program
... # Author: Garret Braman
... # Creation Date: April 28, 2023
... # Below is a simple program with several.  You need to identify the issues and correct them.
... 
... import random
... import time
... 
... def displayIntro():
... 	print('''You are in a land full of dragons. In front of you,
... 	you see two caves. In one cave, the dragon is friendly
... 	and will share his treasure with you. The other dragon
... 	is greedy and hungry, and will eat you on sight.''')
... 	print()
... 
... def chooseCave():
...     cave = ''
...     #the indention on the while below was incorrect. I think you want to indent like the following: 
...     while cave != '1' and cave != '2':
...         #while cave != '1' and cave != '2':
...             #The indention on the print fucntion now needs corrected since the while loop indention was corrected. 
...       print('Which cave will you go into? (1 or 2)')
...             #print('Which cave will you go into? (1 or 2)')
...             #The indention on the input fucntion now needs corrected since the while loop indention and print function indention was corrected. 
...       cave = input()
...             #cave = input()
... 
...     #the return is incorrect as caves is not supposed to be plural. It must match the defenition given above. Try this:
...     return cave
    #return caves

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    #the following function makes the user wait 3 seconds instead of 2. Change to:
    time.sleep(2)
    #time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        #there is no parenthesis behind in the print function. Try this:
      print('Gobbles you down in one bite!')
        #print 'Gobbles you down in one bite!'


displayIntro()
#the choosecave funciton does not match the defined one above. The C in cave must be capitalized:
caveNumber = chooseCave()
#caveNumber = choosecave()
checkCave(caveNumber)

#Make sure that all spellings are correct. I think "Thanks for playing" is what was meant to be stated:
print("Thanks for playing")
#print("Thanks for planing")
