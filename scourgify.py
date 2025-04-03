""" 
In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. 
Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
 """

import csv
import sys

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
            file_path_to_rd = sys.argv[1]
            file_path_to_wr = r"D:\CODING!!!\Project Python\practice_exercise\after.csv"

            with open(file=file_path_to_rd, mode='r') as file1:
                with open(file=file_path_to_wr, mode='a') as file2:
                    reader = csv.DictReader(file1)
                    writer = csv.DictWriter(file2, fieldnames=['first', 'last', 'house'])
                    for row in reader:
                        name = row['name']
                        street = row['house']
                        f_name, l_name = name.split(',')
                        print(f'{f_name}, {l_name}, {street}')                   
                        
                        # writer.writeheader({'first', 'last', 'house'})
                        writer.writerow({'first': f_name.strip(" "), 'last': l_name.strip(" "), 'house': street})
      


            

    except FileNotFoundError:        
        print(f'File does not exist')
        sys.exit()

    except ValueError:
        sys.exit()


if __name__ == "__main__":
    main()
