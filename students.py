######################## CSV #######################################
""" 
In the terminal: code ../my_files/students.csv
 """


students = []
people = []
file_path = "D:\CODING!!!\Project Python\my_files\students.csv"

with open(file=file_path, mode='r') as file:
    for line in file:
        """ row = line.rstrip().split(',')
        print(f'{row[0]}, \t {row[1]}') """

        name, house = line.rstrip().split(',')

        students.append(f'{name} lives in {house}')
        
        person = {'name': name, 'house': house}
        people.append(person)
        """ people.append({'name': name, 'house': house}) """



    # students array 
    print("\n Students (Sorted)")
    for student in sorted(students):
        print(student)

    # students dictionary list (can't call sorted())
    print("\n People (Unsorted)")
    for person in people:
        print(f"{person['name']} lives in {person['house']}")

    # Here is the sort for the at=rray of dictionary ####
    # Create a function for dict sort
    def get_name(person):
        return person['name']
    
    print("\n People (dict sort approach (Sorted)")
    try:
        for person in sorted(people, key=get_name):
            print(f'{person['name']} lives in {person['house']}')

    except KeyError as e:
        print(f'ERROR: {e}')
    
    ###### Lambda function for finding the key, sort the dictionary (Lambda expression) ####
     # lambda_expr ::= "lambda" [parameter_list] ":" expression 
     # https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-parameter_list


    print("\n People (Sorted)")
    try:
        for person in sorted(people, key=lambda person: person['name']):
            print(f'{person['name']} lives in {person['house']}')
    
    except KeyError as e:
        print(f"ERROR: {e}")


""" 
students2.csv

The ValueError: too many values to unpack error produced by the interpreter is a result of the fact 
that we previously created this program expecting the CSV file is split using a , (comma). 
We could spend more time addressing this, but indeed someone else has already developed a way to “parse” (that is, to read) CSV files!

Python’s built-in csv library comes with an object called a reader. As the name suggests, 
we can use a reader to read our CSV file despite the extra comma in “Number Four, Privet Drive”. 
A reader works in a for loop, where each iteration the reader gives us another row from our CSV file. 
 """
import csv

file_path2 = "D:\CODING!!!\Project Python\my_files\students2.csv"

with open(file=file_path2) as file:
    reader = csv.reader(file)
    for row in reader:
        people.append({'name': row[0], 'house': row[1]})

    
    try:
        print("\n sorted list: multi-length value")
        for person in sorted(people, key=lambda person: person['name']):
            print(f'{person['name']} lives in {person['house']}')

    except KeyError as e:
        print(f'ERROR: {e}')


################# To directly access the row dictionary, getting the name and home of each student as labeled in csv headers. ############### 

file_path3 = "D:\CODING!!!\Project Python\my_files\students2.csv"

with open(file=file_path3) as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append({'name': 'name', 'house': 'home'})

    
    try:
        print("\n sorted list: multi-length value with DictReader")
        for person in sorted(people, key=lambda person: person['name']):
            print(f'{person['name']} lives in {person['house']}')

    except KeyError as e:
        print(f'ERROR: {e}')





    

     



