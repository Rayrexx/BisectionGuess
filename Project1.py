high = 100
low = 0
print("Please think of a number between 0 and 100!")
input("Press 'x' to continue ")
guess = int((high + low)/2)
while guess <= 100:
    print("Is your secret number ",guess,"?")
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if inp == 'h':
        high = guess
        guess = round((high + low)/2)
    elif inp == 'l':
        low = guess
        guess = round((high + low)/2)
    elif inp == 'c':
        print("Game over. Your secret number was: " ,guess)
        break
    else:
        print("Sorry, I did not understand your input.")
