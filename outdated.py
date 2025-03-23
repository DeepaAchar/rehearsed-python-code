""" 
In a file called outdated.py, implement a program that prompts the user for a date,
anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
wherein the month in the latter might be any of the values in the list below:

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, 
prompt the user again. Assume that every month has no more than 31 days; 
no need to validate whether a month has 28, 29, 30, or 31 days.
 """

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

global formatted_date

def format_date():
    while True:
        try:
            prompt = input("Enter the date in month/day/year: ")
            if '/' in prompt:
                mm, dd, yyyy = prompt.split('/')
            else:
                mm, dd, yyyy = prompt.split(" ")
                dd = dd.strip(',')
                
            # print(mm + ',' + dd + ',' + yyyy)

            if 0 < int(dd) < 31: 
                # if mm in month and 0 < int(dd) < 31:
                if isinstance(mm, str):
                    if mm in month:
                        format_m = str(month.index(mm) + 1).zfill(2)
                        mm = str(format_m).zfill(2)
                        dd = str(dd).zfill(2)
                        formatted_date = f'{yyyy}-{mm}-{dd}'
                        print(formatted_date)
                        return formatted_date            
                    
                    elif 0 < int(mm) < 12:
                        mm = str(mm).zfill(2)
                        dd = str(dd).zfill(2)
                        formatted_date = f'{yyyy}-{mm}-{dd}'
                        print(formatted_date)
                        return formatted_date
                    
                    else:
                        print("Invalid month")
                        raise ValueError
                        # prompt = input("Enter the date in month/day/year: ")

            else:
                print("Inavlid day")
                raise ValueError
                # prompt = input("Enter the date in month/day/year: ")
                    
        except ValueError:
            print("Invalid input")
            pass

def main():
    prompt = format_date()
    # print(prompt)

main()