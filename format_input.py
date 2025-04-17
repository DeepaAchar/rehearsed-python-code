def typical_approach(s):
    f_name, l_name = s.split(',')
    name = f'{f_name} {l_name}'
    print(f'Hello, {name}')

import re
def re_approach(s):
   
   # matches = re.search(r"^(.+),(.+)$", s)
   # Handle 0-any spaces between first & last name
    matches = re.search(r"^(.+), *(.+)$", s)
    if matches:
       """ f_name, l_name = matches.groups()
       name = f'{f_name} {l_name}' """
       name = matches.group(2) + " " + matches.group(1)
       print(f'Hello, {name}')

    print("\n Approach#2 using walrus operator := \n")
    # using := operator
    if extracted_name := re.search(r'^(.+), *(.+)$', s):
        name = extracted_name.group(2) + ' ' + extracted_name.group(1)
        print(f'Hello, {name}')

def main():
    prompt = input("Enter your comma separated full name: ").strip()
    print("\n Approach#1 \n")
    output_1 = typical_approach(prompt)

    print("\n Approach#2 \n")
    output_1 = re_approach(prompt)

if __name__ == "__main__":
    main()

