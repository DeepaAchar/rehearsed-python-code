def main():
    time = input("Meal Planner: What time is it (hr:min)? ").strip().lower()
    converted_time = convert_24hr(time)

    if 7 <= float(converted_time) <= 8:
        print("Breakfast Time!")
    elif 12 <= float(converted_time) <= 13:
        print("Lunch Time!")
    elif 18 <= float(converted_time) <= 19:
        print("Dinner Time!")
    else:
        print("Not a meal time " + "🙁" + "!!!")

def convert_24hr(time):
    hours, minutes = time.split(":")

    # System for 24 hr clock
    minutes = float(minutes) / 60
    # print("minutes:" + f"{minutes:.1f}")
    # print("hours:" + hours)
    temp = float(hours) + minutes
    return temp

if __name__ == "__main__":
    main()