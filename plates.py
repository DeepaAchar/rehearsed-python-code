def main():
    plate = input("Plate: ")
   
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# All vanity plates must start with at least two letters.”
#… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# No periods, spaces, or punctuation marks are allowed.”


def is_valid(s):
    special_characters = ".!' '"
    for c in s:
        if c in special_characters: 
            print("Invalid character \n")
            return False

    if 1 < len(s) < 7:
        prefix = s[0:2]
        for c in prefix:
            if c.isdigit():
                print("Invalid length \n")
                return False
            
        suffix = s[2:len(s)]
        reversed_str = suffix[:: -1]
        if suffix.isalnum():

            # Verify that str does not contain number sequence anywhere in the middle of the str
            for i in range(len(reversed_str)-1):
                if reversed_str[i].isalpha():
                    if reversed_str[i+1].isdigit():
                        print("Invalid numeric substring \n")
                        return False
                    
            # Verify that number sequence does not start with 0 
            for i in range(len(suffix)):
                if suffix[i].isalpha():
                    break
                else:
                    # if not non_zero_integer(suffix[i:len(s)]):
                    if not non_zero_integer(suffix[i]):
                        print("Invalid number sequence ##1 \n")
                        return False
                    else:
                        return True
                    
        elif suffix.isdigit():
            if not non_zero_integer(suffix[0]):
                print("Invalid number sequence ##2 \n")
                return True
            else:
                return False
        
        else:
            return True
    
    else:
        print("Invalid! Oversize string \n")
        return False
        
def non_zero_integer(n):
    if int(n[0]) == 0:
        return False
    return True

main()