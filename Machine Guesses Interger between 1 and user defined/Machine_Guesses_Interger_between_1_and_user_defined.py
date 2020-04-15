
import time

print()
print ("Pick any number above 1")
maximum_string = input()

if str.isdigit(maximum_string):
    print()
else:
    print("\n You must input an interger, a whole number.")

maximum = int(maximum_string) + 1
minimum = 0

    
print("\n Now think of a number between 1 and " + maximum_string + ". \n I'm going to guess it.")
guess= maximum//2


time.sleep(4)


print("\n Is your number " + str(guess) + "?")
guess_correct = input(["yes or no"])
guess_correct = guess_correct.lower()

if guess_correct == ("yes"):
    print("\n I'm so smart")
    guessing_time = False
            
elif guess_correct == ("no"):
    print("\n Is the number higher or lower?")
    guessing_time = True
    guess_correct = input()

else:
    print ("You're going to have to try to type yes or no correctly next time. Bye!")

#this code breaks easily if the user doesn't respond with the canned yes/no then higher/lower/yes

#guessing_time is triggered by a no response
while guessing_time:

    if guess_correct == ("lower"):
        maximum = guess
        guess = (int(maximum) + int(minimum))//2
        print("\n Is your number " + str(guess) +", higher, or lower?")
        guess_correct = input()
        guess_correct = guess_correct.lower()

    elif guess_correct == ("higher"):
        minimum = guess
        guess = (guess + maximum)//2
        print("\n Is your number " + str(guess) +", higher, or lower?")
        guess_correct = input()
        guess_correct = guess_correct.lower()

    elif guess_correct == ("yes"):
        print("\n I'm so smart")
        guessing_time = False

    else:
        print("Select lower, higher or yes.")
        guess_correct = input()
        guess_correct = guess_correct.lower()


print("\n Thanks for playing. Bye! \n")