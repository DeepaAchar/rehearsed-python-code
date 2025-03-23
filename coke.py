def buy_coke():
    amount_due = 50
    payment = 0

    while True:
        if amount_due > 0:
            payment = int(input("Insert coin (5, 10, 25): ")) 
            if payment not in {5, 10, 25}:
                print(f"Amount Due: {amount_due}")
            else:
                amount_due -= payment
                print(f"Amount Due: {amount_due}")
                
        elif amount_due == 0:
            print("Here is your COKE!!!")
            print(f"Change Owed: {amount_due}")
            break
        else:
            print("Here is your COKE!!!")
            print(f"Change Owed: {amount_due * -1}")
            break

def main():
    buy_coke()

main()

    