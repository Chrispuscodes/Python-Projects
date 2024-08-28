import random

top_of_range = input ('Type a number: ')

if top_of_range.isdigit(): #if the answer is and integer, it'll return true
    top_of_range = int(top_of_range) #and this will turn it intoan integer
    if top_of_range <=0:
        print ('Please type a number greater than 0 next time.')
        quit()

else:
    print('please type anumber next time.')
    quit()
random_number = random.randrange(-5,11)  #the number 11 does not show up in the sequence. the numbers end at 10
guesses = 0 # track the number of guesses
#alternative random_number = random.randint(-5,11)

while True:
    guesses +=1
    user_guess = input('Make a guess: ')

    if user_guess.isdigit(): 
       user_guess = int(user_guess)   
    else:
        print('please type anumber next time.')
        continue #Automatically brings us back to the loop
    if user_guess == random_number:
        print ('you got it!')
        break
    elif user_guess > random_number:
            print('You were above the number!')
    else:
            print ('You were below the number!')

print ('You got it in', guesses, 'guesses')

