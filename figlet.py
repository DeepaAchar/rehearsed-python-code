# figlet.org/examples.html
'''
In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
 - Zero if the user would like to output text in a random font.
 - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
'''

import random
from pyfiglet import Figlet
import sys

def _FIGlet_art():
    figlet = Figlet()
    fonts_list = figlet.getFonts()
    try:
        arg_count = sys.argv
        if len(arg_count) == 1:
            print(fonts_list[2])
            prompt = input("Enter the sentence: ")

            # def setFont(self, **kwargs)
            # Note: **kwargs are 'keyword arguments'
            figlet.setFont(font = random.choice(fonts_list)) 
            print(figlet.renderText(prompt))
            return


        elif len(arg_count) == 3:            
            if sys.argv[1] == "-f" or "--font":
                prompt = input("Enter the sentence: ")
                figlet.setFont(font = sys.argv[2])
                print(figlet.renderText(prompt))
                return

        else:
            print("Invalid call")
            sys.exit()
 
    except IndexError:
        print("Invalid FONT!!!" + "Font lookup: http://www.figlet.org/examples.html")
        sys.exit()
        pass
    
def main():
    _FIGlet_art()


main()