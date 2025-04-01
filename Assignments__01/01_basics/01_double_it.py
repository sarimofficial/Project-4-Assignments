while True:
    try:
        curr_value = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

while curr_value < 100:
    curr_value *= 2  # Same as curr_value = curr_value * 2
    print(curr_value, end=' ')

print()