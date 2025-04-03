""" 
In a file called pizza.py, implement a program that expects exactly one command-line argument, 
the name (or path) of a CSV file in Pinocchio’s format, 
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. 
    - Format the table using the library’s grid format. 

If the user does not specify exactly one command-line argument, 
or if the specified file’s name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit.
 """
import sys
import csv
from tabulate import tabulate

def main():
        
    try:
        args = len(sys.argv)

        if args < 2:
            print(f'Too few command-line arguments')
            raise ValueError
        
        elif args > 2:
            print(f'Too many command-line arguments')
            raise ValueError

        else:
            file_path = sys.argv[1]

            tmp = file_path.split('\\')[::-1]
            file_ext = tmp[0].split('.')[::-1]

            if file_ext[0] != "csv":
                print(f'Not a CSV file')
                raise ValueError

            else:
                with open(file=file_path, mode='r') as file:
                    reader = csv.DictReader(file)
                    table = []
                    t_row = {}                   
                    
                    # print(tabulate(table, headers))
                    if file_ext[1] == "sicilian":
                        header_1 = "Sicilian Pizza"
                        for row in reader:
                            headers = [header_1, "Small", "Large"]
                            t_row = {row['Sicilian Pizza'], row['Small'], row['Large']}
                            table.append(t_row)

                    elif file_ext[1] == "regular":
                        header_1 = "Regular Pizza"
                        for row in reader:
                            headers = [header_1, "Small", "Large"]
                            t_row = {row['Regular Pizza'], row['Small'], row['Large']}
                            table.append(t_row)                      
                    
                    print(tabulate(table, headers, tablefmt="grid"))

    except FileNotFoundError:
        print(f'File does not exist')
        sys.exit()

    except ValueError:
        sys.exit()


if __name__ == "__main__":
    main()

