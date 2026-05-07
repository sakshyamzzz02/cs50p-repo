def main():
    time = input("Enter the time: ")
    T= convert(time)

    if 7 <= T <= 8:
        print("breakfast time")
    elif 12 <= T <= 13:
        print("lunch time")
    elif 18 <= T <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.strip().split(":")
    hours = int(hours)
    minutes = int(minutes)

    t = hours + (minutes / 60)

    #for the am/pm format:
    
    # if pm and not 12
    # t = t + 12
    # elif am and 12
    # t = minutes / 60

    return t


if __name__ == "__main__":
    main()
