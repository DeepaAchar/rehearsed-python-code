emoticon = "V.V"

SHOWS = [
 " Avatar: The last airbender",
 "Ben 10",
 "Arthur",
 " Spongebob Squarepants",
 "Phineas and ferb",
 "Kim possible",
 "Jimmy Neutron ",
 "the Proud family "
]

def greet(input):
    if "Hi" in input:
        return "Hi, there!" 
    return "I'm not sure what do you mean?"

def say(phrase):
    print(phrase + " " + emoticon)

def askUser():
    u_name = input("What's your name? ")
    if u_name == "":
        return "No NAME"
    return u_name

def getUserName():
    return askUser()

def guessMyAge():
    guess = int(input("Guess my age:"))
    return guess

def main():
    global emoticon
    say("Is anybody home?")
    emoticon = ":D"
    say("Oh! Hi!")

    print(getUserName())

    guess = guessMyAge()
    if guess == 25:
        print ("correct!")
    else:
        print("Incorrect! Better luck next time!")

    print("Let's Title all!")
    formatted_content = []
    for show in SHOWS:
       formatted_content.append(show.strip().title())
    print(formatted_content)
    print ("\n Final List! \n")
    print(', '.join(formatted_content))
 
main()