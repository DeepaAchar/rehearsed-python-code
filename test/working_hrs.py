""" 
In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below 
and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). 
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. 
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats 
or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). 
But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours 
    (e.g., 5:00 PM to 9:00 AM).
 """

import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        if matches := re.match("^([0-9][0-2]?):?([0-5][0-9])? ([A|P][M]) to ([0-9][0-2]?):?([0-5][0-9]?)? ([A|P][M])$", s):
            # print(f'{matches.group(1)}, {matches.group(2)}, {matches.group(3)}, {matches.group(4)}, {matches.group(5)}, {matches.group(6)}')

            if matches.group(3) == "AM":
                begin = 0 + int(matches.group(1))
            if matches.group(6) == "AM":
                end = 0 + int(matches.group(4))
            if matches.group(3) == "PM":
                begin = (12 + int(matches.group(1))) % 24
            if matches.group(6) == "PM":
                end = (12 + int(matches.group(4))) % 24
            if matches.group(2) != None:
                b_min = matches.group(2)
            else:
                b_min = 0
            if matches.group(5) != None:
                e_min = matches.group(5)
            else:
                e_min = 0    

            return (f'{begin:02}:{b_min:02} to {end:02}:{e_min:02}')

        else:
            raise ValueError
    
    except ValueError:
        sys.exit("Invalid")

if __name__ == "__main__":
    main()
