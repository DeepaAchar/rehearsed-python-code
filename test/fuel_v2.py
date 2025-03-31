""" 
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:
convert expects a str in X/Y format as input, wherein each of X and Y is an integer, 
and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. 
If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. 
If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
 """
import sys

def main():
    prompt = input("Enter the fraction (format: x/y): ")
    output = convert (prompt)
    print(output)
           
        
def convert(fraction):  
       
        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)

            if not isinstance(x, int) or not isinstance(y, int):
                raise ValueError
                
            elif y == 0:
                raise ZeroDivisionError

            elif x > y:
               raise ValueError
                 
            else:
                tank = float(gauge(x/y))
                # print(f'z: {tank}')
                if tank <= 1.00:
                    return 'E'
                elif tank >= 99.00:
                    return 'F'
                else:
                    return str(f'Fuel Available: {tank: .2f}') + '%'
            
        except ValueError:
            print("Numerator can't exceed denominator!")

        except ZeroDivisionError:
            print("ZERO denominator")

        except EOFError:
            sys.exit() 


def gauge(percentage):
    value = percentage * 100
    return value


if __name__ == "__main__":
    main()