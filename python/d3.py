num = int(input("enter number"))

if num%4==0:
    if num%100==0:
        if num%400==0:
            print(num,"is a leap year")
        else:
            print("not a leap year")
    else:
        print("year is leap year")
else:
    print(num,"is not leap year")
    5
