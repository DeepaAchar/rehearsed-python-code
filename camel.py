def convert_camel_to_snake_case():
    prompt = input("Enter your camel case variable: ")

    str_updated = ""
    for c in prompt:
        if c.islower(): 
            # print("Skip")
            str_updated = str_updated + c
        else:
            str_updated = str_updated + '_' + c.lower()
    return str_updated

def main():
    prompt = convert_camel_to_snake_case()
    print(prompt)

main()