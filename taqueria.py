menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def order_your_food():
    bill = 0
    try:
        while True:
            item = input("Enter your order (press Ctrl+Z to exit): ").title()
            # print(f'{item}')
           
            if item in menu.keys():
                bill += menu[item]

    except (EOFError, KeyError):
        pass

    return bill


def main():
    your_bill = order_your_food()
    print(f'Your bill: {your_bill:.2f}')
main()



    
