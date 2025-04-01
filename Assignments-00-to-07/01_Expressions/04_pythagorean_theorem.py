import math

def calculate_hypotenuse():
    while True:
        try:
            ab = float(input("Enter the length of AB: "))
            ac = float(input("Enter the length of AC: "))
            bc = math.sqrt(ab**2 + ac**2)
            print(f"\nThe length of BC (the hypotenuse) is: {bc:.1f}\n")
            break
        except ValueError:
            print("Invalid input. Please enter numeric values for the lengths.")

if __name__ == "__main__":
    calculate_hypotenuse()