""" 
An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, 
akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. 
But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! 
If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, 
respectively, if that input is a valid IPv4 address or not.

 """
import re
import sys


def main():

    output = validate(input("IPv4 Address: "))
    
    if output == True:
        print("Valid")
    else:
        sys.exit("Invalid")

def validate(ip):
    if matches := re.search(r"^(\d?\d?\d?)\.(\d?\d?\d?)\.(\d?\d?\d?)\.(\d?\d?\d?)$", ip):
        # print(f'{matches.group(1)}, {matches.group(4)}')
        if 0 <= int(matches.group(1)) < 256 and 0 <= int(matches.group(2)) < 256 and 0 <= int(matches.group(3)) < 256 and 0 <= int(matches.group(4)) < 256:   
            # print(f'{matches.group(1)}, {matches.group(4)}')
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()