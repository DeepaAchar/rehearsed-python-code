# https://pypi.org/project/inflect/ - Correctly generate plurals, singular nouns, ordinals, indefinite articles

"""
 implement a program that prompts the user for names, one per line, 
 until the user inputs control-d. Assume that the user will input at least one name. 
 Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 
 names with  commas and one
"""

import inflect
import sys

def adieu():
    guest_list = []
    p = inflect.engine()
    print("Enter your guest list one per line: ")
    while True:
        try:
            prompt = input("\n Name: ")
            guest_list.append(prompt)

        except EOFError:
            break       
    
    print("Adieu, adieu, to " + p.join(guest_list))

def main():
    adieu()

main()