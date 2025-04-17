from validator_collection import validators, checkers

def syntax_validation_for_email(s):
    validate = checkers.is_email(s)
    return validate

def main():
    prompt = input("What's your email address? ")
    is_valid = syntax_validation_for_email(prompt) 
    if is_valid:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__" :
    main()