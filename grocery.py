grocerry_list = {}

def add_item():
    try:
        while True:
            prompt = input("Add an item: ")
            item = prompt.upper()

            if item in grocerry_list:
                grocerry_list[item] += 1
            else:
                grocerry_list[item] = 1

    except (KeyError, EOFError):
        pass

    return grocerry_list


def main():
    your_list = add_item()
    # print(your_list)
    for item in grocerry_list.keys():
        print(f'{grocerry_list[item]} \t {item}')


main()
            

