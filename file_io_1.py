#################### File IO #################################### 
import os

directory = "D:\CODING!!!\Project Python\my_files"
os.makedirs( directory, exist_ok=True)


# file_path = os.path.join(directory, "Bio.txt")
file_path_2 = os.path.join(directory, "grocery_list.txt")
# file = open(file_path, 'w')
# rm Bio.txt in the terminal to remove the file

#---------File writes....------------#
""" file = open(file_path, 'a')
file.close() """

# The keyword with allows you to automate the closing of a file.
""" print("########### Your_Bio ######################")
prompt = input('\n') 
with open(file_path, 'a') as file:
    file.write(f'{prompt} \n') """

""" print("########### List Your Grocery ######################")
prompt = input('\n')
with open(file_path_2, 'a') as file:
    file.write(f'{prompt} \n') """


#---------File reads....------------#

""" with open(file_path, 'r') as file:
    lines =  file.readlines()

for line in lines:
    print('- '+ line.rstrip()) """

""" with open(file_path, 'r') as file:
    for line in file:
        print('- '+ line.rstrip()) """

g_list = []
with open(file_path_2, 'r') as file:
    for line in file:
        g_list.append(line.rstrip())

for item in sorted(g_list):
    print(f'{item}, ')



