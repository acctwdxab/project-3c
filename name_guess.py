secret = int ( input ( 'Enter the number for the player to guess.\n'))
guess = int ( input ( 'Enter your guess\n' ) )
tries = 0
while guess != secret :
    if guess > secret :
        guess = int ( input ( 'Too high - try again:\n' ) )
    tries = tries + 1
    if guess < secret:
        guess = int ( input ( 'Too low - try again:\n' ) )
        tries = tries + 1
else: guess == secret
tries = tries + 1
print ( 'You guessed it in' , tries , "tries." )
