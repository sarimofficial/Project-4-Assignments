from collections import Counter

numbers = []
while True:
    user_input = input("Enter a number: ").strip()
    if not user_input:
        break
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("Please enter a valid number.")

counts = Counter(numbers)
for num in sorted(counts):
    print(f"{num} appears {counts[num]} time{'s' if counts[num] != 1 else ''}.")