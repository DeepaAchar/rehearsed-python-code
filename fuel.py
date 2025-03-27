""" 
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, 
wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, 
how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
 """
# https://docs.python.org/3/tutorial/errors.html

import sys

def fuel_monitor():
    while True:
        try: 
            prompt = input("Enter the fraction (format: x/y): ")
            x, y = prompt.split('/')

            x = int(x)
            y = int(y)
                             
            if y == 0:
                raise ZeroDivisionError 
            elif x > y:
                raise ValueError 
            else:
                tank =  x / y * 100
                # print(f'z: {tank}')
                if tank <= 1:
                    return 'E'
                elif tank >=99:
                    return 'F'
                else:
                    return str(f'Fuel Available: {tank: .2f}') + '%'

                
        except ValueError:
           print("Raise: ValueError")
           pass

        except ZeroDivisionError:
            print("Raise: Zero denomenator")
            pass

        
def main():
    output = fuel_monitor()
    print(output)

main()