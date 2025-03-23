def main():
    time = input("Meal Planner: What time is it? ").strip().lower()
    if time.endswith("am"):
        converted_time = convert_12hr(time.removesuffix("am"))
    elif time.endswith("pm"):
        converted_time = convert_12hr(time.removesuffix("pm"))
        
    
    if 7 <= float(converted_time) <= 8 and time.endswith("am"):
        print("Breakfast Time!")
    elif 12 == float(converted_time) and time.endswith("pm"):
        print("Lunch Time!")
    elif 6 <= float(converted_time) <= 7 and time.endswith("pm"):

        print("Dinner Time!")
    else:
        print("Not a meal time " + "🙁" + "!!!")


def convert_12hr(time):
    hours, minutes = time.split(":")

    # System for 24 hr clock
    minutes = float(minutes) / 60
    # print("minutes:" + f"{minutes:.1f}")
    # print("hours:" + hours)
    temp = float(hours) + minutes
    return temp

if __name__ == "__main__":
    main()