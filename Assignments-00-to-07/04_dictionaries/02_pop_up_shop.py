fruit_prices = {
    'apple': 1.5,
    'durian': 15.0,
    'jackfruit': 10.0,
    'kiwi': 2.5,
    'rambutan': 3.0,
    'mango': 2.0
}

quantities = {}
total = 0.0

print("Fruit Shop Calculator\n")

for fruit in fruit_prices:
    while True:
        try:
            qty = int(input(f"How many ({fruit}) do you want?: "))
            if qty >= 0:
                quantities[fruit] = qty
                total += qty * fruit_prices[fruit]
                break
            print("Quantity cannot be negative!")
        except ValueError:
            print("Please enter a whole number.")

print("\nReceipt:")
for fruit, qty in quantities.items():
    if qty > 0:
        print(f"{fruit.title()}: {qty} × ${fruit_prices[fruit]:.2f} = ${qty * fruit_prices[fruit]:.2f}")

print(f"\nYour total is ${total:.2f}")