MIN_HEIGHT = 50

while True:
    height_input = input("How tall are you? ").strip()
    
    # Exit if user enters nothing
    if not height_input:
        break
    
    try:
        height = int(height_input)
        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")
    except ValueError:
        print("Please enter a valid number for height.")