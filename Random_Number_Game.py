# This program asks the user to guess a number to see if it matches a random number generated between 0 and 20

from random import randint
response = ''

while not (response == 'no' or response == 'No' or response == 'NO' or response == 'n' or response == 'N'):
    print('\nHello, let us play the random number game. What is your name?')
    name = input()
    secretnumber = randint(0,20) # Random number generator
    print('\nNice to meet you, ' + name + '. I am guessing a number between 0 and 20. I will give you 6 guesses to guess the correct number. \n\nLet us begin, shall we?', end = '\n\n')
    
    # Loop for 6 times to give user 6 tries to guess the correct number. Break when user guesses correctly or when 6 tries are up.
    for GuessesinGuess in range(1,7):
        if GuessesinGuess == 1: # Modify the question that is asked based on the attempt count
            print('Take your first guess.')
        elif GuessesinGuess > 1 and GuessesinGuess <= 5:
            print('Take another guess.')
        elif GuessesinGuess == 6:
            print('Take another guess. Remember this is your last attempt!!!')
            
        guess = input() # Ask for their guess each time
        
        if (int(guess) > secretnumber and GuessesinGuess == 6) or (int(guess) < secretnumber and GuessesinGuess == 6): # Go to break loop if they are on their last guess
            break
        elif int(guess) > secretnumber:
            print('Nice try, ' + name + '. But, ' + str(guess) + ' is too high. Guess lower!', end = '\n\n') # Response if guess is too high
        elif int(guess) < secretnumber:
            print('Nice try, ' + name + '. But, ' + str(guess) + ' is too low. Guess higher!', end = '\n\n') # Response if guess is too low
        else:
            break
    
    # Break loop success statement or failure statement
    if int(guess) == secretnumber:
        print('Awesome job, ' + name + '. You have guessed correctly!', end = '\n\n')
    else:
        print('Sorry, ' + name + ', you have exceeded your 6 attempts :( Maybe next time.', end = '\n\n')
        
    # Ask user if they want to play again
    print('Would you like to play again? Yes or No'); 
    response = input()
    print('')
