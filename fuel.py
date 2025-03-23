# https://docs.python.org/3/tutorial/errors.html

def fuel_monitor():
    while True:
        prompt = input("Enter the fraction (format: x/y): ")
        x, y = prompt.split('/')
        try:
            x = int(x)
            y = int(y) 

            if x <= y:
                break

        except (ValueError, ZeroDivisionError):
            pass

    tank =  float((x / y)) * 100
    # print(f'z: {tank}')
    if tank <= 1:
        return 'E'
    elif tank >=99:
        return 'F'
    else:
        return str(f'Fuel Available: {tank: .2f}') + '%'

def main():
    output = fuel_monitor()
    print(output)

main()