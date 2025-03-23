def einstein():
    c = 300000000
    m = int(input("Enter the mass as an integer:"))
    return int(m*c*c)


def main():
    print("E:" + str(einstein()))

main()