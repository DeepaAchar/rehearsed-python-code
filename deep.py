def answerMachine():
    prompt = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    if(
        prompt == str(42) 
        or prompt == "forty-two"
        or prompt == "forty two"
        # or prompt.startswith("forty")
        ):
        return "Yes"
    return "No"

def main():
    prompt = answerMachine()

     # imoticons: https://emojipedia.org/
    if(prompt.startswith("Y")):
        print("Agreed!" + "🙂")
    else:
        print("Do not agree!" + "🙁")
main()