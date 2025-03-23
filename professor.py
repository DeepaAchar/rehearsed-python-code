""" 
In a file called professor.py, implement a program that:
Prompts the user for a level, n.
If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = ,
wherein each of X and Y is a non-negative integer with digits. 
No need to support operations other than addition (+).

Prompts the user to solve each of those problems. 
If an answer is not correct (or not even a number), 
the program should output EEE and prompt the user again, 
allowing the user up to three tries in total for that problem.

If the user has still not answered correctly after three tries, 
the program should output the correct answer.

The program should ultimately output the user’s score: the number of correct answers out of 10.
 """
import random
import sys

global attempts
global score

def math_quiz():

    while True:
        try:
            level = int(input("Enter level among 1,2,3: "))

            score = 0
            total_questions =  10
            
            i = total_questions
            if 0 < level < 4:
                if level == 1:
                    n = 10
                elif level == 2:
                    n = 50
                else:
                    n = 100

                while i > 0:
                    attempts = 3
                    x = random.randint(1, n)
                    y = random.randint(1, n)
                    output = x + y

                    while attempts > 0:
                        print("You have " + str(attempts) + " attempts remaining")
                        prompt = int(input(str(x) + ' + ' + str(y) + ' = ' ))

                        if isinstance(prompt, int) and (prompt == output):
                            print("Well done!!!")
                            score += 1
                            break
                        
                        else :
                            print("EEE")
                            attempts -= 1

                    i -= 1

                print("Good attempt!")
                print("Here is your final score: " + str(score) + " out of " + str(total_questions))
                return

            else:
                raise ValueError
            
        except ValueError:
            pass

        except EOFError:
             sys.exit()    

def main():
    math_quiz()


main()