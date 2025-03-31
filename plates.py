""" 
############################### Vanity Plates #################################
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

- All vanity plates must start with at least two letters.
- … vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
- Numbers cannot be used in the middle of a plate; they must come at the end. 
        For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
-  The first number used cannot be a ‘0’.
- “No periods, spaces, or punctuation marks are allowed.

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or 
Invalid if it does not. Assume that any letters in the user’s input will be uppercase. 
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. 
Assume that s will be a str.
 """
import sys


def main():
    prompt = input("Eneter your license plate number: ")
    output = is_valid(prompt)
    print(output)


def is_valid(s):
    banned_characters = ".!' '"
    
    try:

        if (len(s) < 2 or (s[1:2].isalpha() == False)):
            raise ValueError
        
        elif len(s) > 6:
            raise ValueError
        
        
        elif s.isalpha():
            return "Valid"
               
        else:
            for c in s:
                if c in banned_characters:
                    print("Invalid character: "+ c)
                    raise ValueError
                    
                elif c.isdigit():
                    if int(c) == 0:
                        raise ValueError
                        
                    else:
                        x = s.index(c)
                        suffix = s[x:len(s)]

                        for x in suffix:
                            if x.isalpha():
                                raise ValueError
                            elif x in banned_characters:
                                raise ValueError                                
                        return "Valid"                  

    except ValueError:
        print("Invalid")
        sys.exit()


if __name__ == "__main__":
    main()