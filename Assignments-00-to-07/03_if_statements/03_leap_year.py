year = int(input("Enter a year: "))

is_leap = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
    else:
        is_leap = True

print("That's a leap year!" if is_leap else "That's not a leap year.")