""" 
In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, 
restructuring your code per the below, wherein value expects a str as input and returns an int, 
namely 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, 
treating the str case-insensitively. You can assume that the string passed to the value function will not contain any leading spaces. 
Only main should call print.
 """

def main():
    prompt = input("Greet me!\n")
    reward = value(prompt.strip().lower())

    if(reward == 0):
        # print(isinstance(reward, int))
        print("$" + reward + "🫨")
    elif(reward == 20):
        # print(isinstance(reward, int))
        print("$" + reward + "😉")
    else:
        # print(isinstance(reward, int))
        print("$s" + reward + "🤑")


def value(greeting):    
    if(greeting.startswith("h")):
        if("hello" in greeting):
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()