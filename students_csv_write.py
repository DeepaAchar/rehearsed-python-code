import csv

name = input("Student's name? ")
house = input("Student street address? ")

file_path = "D:\CODING!!!\Project Python\my_files\students3.csv"

with open(file=file_path, mode='a') as file:
    writer =  csv.DictWriter(file, fieldnames=['name', 'home'])
    writer.writerow({'name': name, 'home': house})