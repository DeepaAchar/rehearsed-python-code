def convert():
    temp = input ("How are you feeling today? ")

    # imoticons: https://emojipedia.org/
    temp = temp.replace(":<", "🙁")
    temp = temp.replace(":>", "🙂")
    return temp
                        


def main():
    emoji = convert()
    print(emoji)

main()