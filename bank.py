""" 
In a file called bank.py, implement a program that prompts the user for a greeting. 
If the greeting starts with “hello”, output $0. 
If the greeting starts with an “h” (but not “hello”), output $20. 
Otherwise, output $100. 
Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
 """

def rewardsSystem():
    prompt = input("Greet me! ").strip().lower()
    
    if(prompt.startswith("h")):
        if(prompt == "hello"):
            return 0
        else:
            return 20
    else:
        return 100

def main():
     # imoticons: https://emojipedia.org/
     
    reward = rewardsSystem()
    if(reward == 0):
        # print(isinstance(reward, int))
        print("$" + reward + "🫨")
    elif(reward == 20):
        # print(isinstance(reward, int))
        print("$" + reward + "😉")
    else:
        # print(isinstance(reward, int))
        print("$s" + reward + "🤑")
        
main()