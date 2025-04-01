MARS_GRAVITY = 0.378

def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter your Earth weight (kg): "))
            if weight > 0:
                return weight
            print("Weight must be positive!")
        except ValueError:
            print("Please enter a valid number!")

def mars_weight_calculator():
    print("NASA Mars Weight Calculator")
    earth_weight = get_valid_weight()
    mars_weight = earth_weight * MARS_GRAVITY
    print(f"On Mars, you would weigh: {round(mars_weight, 2)} kg")

mars_weight_calculator()