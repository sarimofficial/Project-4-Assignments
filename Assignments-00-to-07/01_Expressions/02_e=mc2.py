import random

def roll_dice():
    die1 = random.randint(1, 6)  # Local variable
    die2 = random.randint(1, 6)  # Local variable
    print(f"Roll: {die1}, {die2}")

def main():
    for _ in range(3):  # Loop three times
        roll_dice()

if __name__ == "__main__":
    main()

# New program for mass-energy equivalence calculation
def mass_energy_equivalence():
    C = 299792458  # Speed of light in m/s
    while True:
        try:
            mass = float(input("Enter kilos of mass: "))
            energy = mass * C**2
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"{energy} joules of energy!\n")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    mass_energy_equivalence()
