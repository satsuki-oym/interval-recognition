# make possible intervals in C major 
c_major = {'major second' : ['C', 'D'], 'major third': ['C', 'E'], 
           'perfect fourth': ['C', 'F'], 'perfect fifth': ['C', 'G'], 
           'major sixth': ['C', 'A'], 'major seventh': ['C', 'B']}

import random
total = 0 
attempts = 0


def ask_one_question() -> int:
    attempts = 1
    # randomly print one interval 
    chosen_key = random.choice(list(c_major.keys()))
    print(c_major[chosen_key])

    # ask for user input 
    answer1 = input('What is the interval? ').lower()

    # evaluate the input 
    while answer1 != chosen_key:
        attempts = attempts + 1 
        print('Try again!')
        answer1 = input('What is the interval? ').lower()
        

        
    print('Correct!')
    return attempts

#counter mechanism        
correct = 0
total = 0

correct = correct + 1
attempts = attempts + ask_one_question()

answer2 = input('Do you want to continue? ')

while answer2.lower() == 'yes':
    attempts = attempts + ask_one_question()
    correct = correct + 1
    answer2 = input('Do you want to continue? ')
    
    
if answer2.lower() != 'yes':
    print('accuracy: ' + str(correct / attempts * 100) + '%')