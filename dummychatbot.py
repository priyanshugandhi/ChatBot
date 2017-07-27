import random
from collections import Counter
from string import punctuation
from math import sqrt
 
yes = ['yes', 'Yes', 'Yeah', 'yeah', 'Yea', 'yea', 'Mhmm', 'mhmm', 'Mhm', 'mhm']
no = ['No', 'no', 'Nah', 'nah']
good = ['Good', 'good', 'Great', 'great', 'Okay', 'okay', 'Ok', 'ok', 'OK']
bad = ['Bad', 'bad', 'Not good', 'not good', 'Not well', 'not well']

random_yes = random.choice(yes)
random_no = random.choice(no)
random_good = random.choice(good)
random_bad = random.choice(bad)

greetings = ['Hola', 'Hello', 'Hi', 'Hey!','hey...']
random_greeting = random.choice(greetings)

print(random_greeting)

name = input('What is your name?')
print('Hello', name,)

question1 = ['How are you?','How are you doing?','How is your day?','How is your day going?']
random_question1 = random.choice(question1)

ur1 = input(random_question1)
if ur1 in good:
    print("That's good")
elif ur1 in bad:
    print("I'm sorry")
else:
    print("I don\'t understand")
