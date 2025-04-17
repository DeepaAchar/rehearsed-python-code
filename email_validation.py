""" 
.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions

^   matches the start of the string
$   matches the end of the string or just before the newline at the end of the string

r"..." raw string
f'...' format string

[]    set of characters
[^]   complementing the set

\d    decimal digit
\D    not a decimal digit
\s    whitespace characters
\S    not a whitespace character
\w    word character, as well as numbers and the underscore
\W    not a word character

A|B     either A or B
(...)   a group
(?:...) non-capturing version (ensures it's matched but not returned)
 """

############ Approach_1 ############ 
def typical_approach(s):
    u_name, domain = s.split('@')
    
    if u_name and '.' in domain and domain.endswith("edu"):
        return True

    elif u_name and '.' in domain and domain.endswith("ac.nz"):
        return True

    else:
        return False

############  Approach_2 ############ 
import re
def re_approach(s):
    # .+@.+ ensures atleast one character before & after teh symbol @
    # [^@]+ means any character except an @
    # ^ at the beginnning validates against that occurance of @ at the beginning of the string. i.e., no space allowed in {u_name}
    # +\. that malan@harvard.edu is regarded as valid, where malan@harvard?edu is invalid

    """ if re.search(".+@.+.edu", s):
        print("Valid") """
    # malan@harvard?edu is read valid. 
    # “escape character” or \ as a way of regarding the . as part of our string instead of our validation expression
    if re.search(r"^[^@]+@[^@]+\.edu$", s):
        return True
    elif re.search(r"^[^@]+@[^@]+\.ac$", s):
        return True
    # Notice that [a-zA-Z0-9_] tells the validation that characters must be between a and z, between A and Z, between 0 and 9 and potentially include an _ symbol
    elif re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", s):
        return True
    elif re.search(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.ac$", s):
        return True
    # replace char-set by \w
    elif re.search(r"^\w+@\w+\.edu$", s):
        return True
    elif re.search(r"^\w+@\w+\.ac$", s):
        return True  
    elif re.search(r"^\w+@\w+\.(com|edu|gov|net|org|ac)$", s):
        return True
    # aut.ac.nz there can be word before the end sequence
    # ignore case using re-flags
    elif re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org|nz)$", s, re.IGNORECASE):
        return True
    # The complete validation looks as follows:
    elif re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", s, re.IGNORECASE):
        return True 
    else:
        return False


def main():

    prompt  = input("Enter your corporate email: ").strip()

    print("\nApproach#1\n")
    verified_outcome = typical_approach(prompt)
    print(verified_outcome)

    print("\nApproach#2\n")
    verified_outcome = re_approach(prompt)

    if verified_outcome == True:
        print("Valid!")

    else:
        print("Invalid email address.")


if __name__ == "__main__" :
    main()
