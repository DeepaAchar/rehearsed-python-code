def payback():
    temp = input("Enter a sentence:")
    return temp.replace(" ", "...")

def main():
    
    formatted_output = payback()
    print(formatted_output)
    
main()