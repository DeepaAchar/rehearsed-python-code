""" 
 In a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, 
 and outputs the number of lines of code in that file, excluding comments and blank lines. 
 If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, 
 or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. 
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.
 """
import sys

def main():

    # file_path = "D:\CODING!!!\Project Python\practice_exercise\deep.py"
    # file_path = "D:\CODING!!!\Project Python\my_files\Bio.txt"

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
            if file_ext[0] != 'py':
                print(f'Not a Python file')
                raise ValueError

            line_count = 0
            with open(file=file_path, mode='r', encoding='utf-8') as file:
                lines = file.readlines()
                for line_number, line in enumerate(lines, start=1):
                    print(f'{line_number} \t {line.rstrip()}')
                    if line.strip() == "" or line.strip().startswith('#'):
                        line_count += 0
                    else:
                        line_count += 1

            print(f'Lines of code: {line_count}')


    except FileNotFoundError as e:
        print(f'File does not exist')
        print(f'ERROR: {e}')
        sys.exit()

    except ValueError as e:
        print(f'ERROR: Unsupported file. {e}')
        sys.exit()



if __name__ == "__main__":
    main()