def rewardsSystem():
    prompt = input("Greet me! ").strip().lower()
    if(prompt == "hello"):
        return "N"
    elif(prompt.startswith("h")):
        return "S"
    else:
        return "Y"

def main():
     # imoticons: https://emojipedia.org/
     
    reward = rewardsSystem()
    if(reward == "N"):
        print("$0" + "🫨")
    elif(reward == "S"):
        print("$20" + "😉")
    else:
        print("$100" + "🤑")

main()