def interpreter():
    x,y,z = input("Write an arithmetic expression for calculation as x y z with a space separator where y is the operator: ").split(" ")

    operand_1 = float(x)
    operand_2 = float(z)
    operator = y

    match operator:
        case "+":
            result = operand_1 + operand_2
        case "-":
            result = operand_1 - operand_2
        case "*":
            result = operand_1 * operand_2   
        case "/":
            if(operand_2 != 0.0):
                result = operand_1 / operand_2
            else:
                result = "Zero Division ERROR! Attempting to devide by ZERO"
                return result
        case _:
            print("No op")

    print(f"Result {result:.1f}")

def main():
    interpreter()

main()