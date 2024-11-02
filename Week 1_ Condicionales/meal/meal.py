def main():
    time = input("What time is it? ")
    ctime = convert(time)
    if ctime >= 7 and ctime <= 8:
        print("breakfast time")
    elif ctime >= 12 and ctime <= 13:
        print("lunch time")
    elif ctime >= 18 and ctime <= 19:
        print("dinner time")

def convert(t):
        if t.endswith("p.m.") == True:
            t = t.replace("p.m.","")
            hours, minutes = t.split(":")
            ctime = float(hours) + (float(minutes) / 60) + 12
            return ctime
        else:
            t = t.replace("a.m.","")
            hours, minutes = t.split(":")
            ctime = float(hours) + (float(minutes) / 60)
            return ctime
if __name__ == "__main__":
    main()
