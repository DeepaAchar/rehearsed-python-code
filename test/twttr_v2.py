
""" 
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, 
restructuring your code per the below, 
wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase.
 """

""" 
if __name__ == "__main__":
    main()

The  check allows developers to separate the logic of the code meant to run directly from the code that can be reused as a module elsewhere. 
 """

def main():
    word = input("Enter the word: ")
    output = shorten(word)
    print(f'"You tweeted: " {output}')


def shorten(word):
    vowels = "AEIOUaeiou"
    your_tweet = ''
    for c in word:
        if c not in vowels:
            your_tweet = your_tweet + c
        else:
            your_tweet = your_tweet + ''

    return your_tweet


if __name__ == "__main__":
    main()