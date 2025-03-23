# pip install emoji
# https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias

import emoji

def convert_emojis():
    prompt = input("Input in English: ")

    # conv_prompt = emoji.get_emoji_by_name(prompt)
    print(emoji.emojize(prompt))
    return emoji.emojize(prompt) 

def main():
    convert_emojis()

main()