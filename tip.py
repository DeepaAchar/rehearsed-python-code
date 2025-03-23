def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # print(str(dollars) + " & " + str(percent))
    tip = dollars * percent / 100
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    temp = d.strip("$")
    return float(temp)

def percent_to_float(p):
   temp = p.strip("%")
   return float(temp)

main()