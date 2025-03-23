""" 
Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. 
. If the guess is not a positive integer, the program should prompt the user again.
. If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
. If the guess is larger than that integer, the program should output Too large! and prompt the user again.
. If the guess is the same as that integer, the program should output Just right! and exit.
 """

import random
import sys

global level 
global guess
global prompt

def guess_a_number():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                n = random.randint(0, level)
                # print("Right guess is " + str(n))
                user_input = input("Guess a number betwween 0  & " + str(level) + ': ')
                prompt = int(user_input)
                if prompt == n:
                    return "Just right!"
                elif 0 <= prompt < n:
                    return "Too small!"
                elif n < prompt < level:
                    return "Too large!"
                else:
                    raise ValueError
            else:
                raise ValueError

        except ValueError:
            pass
        except EOFError:
            sys.exit()
            

def main():
    output = guess_a_number()
    print(output)

main()