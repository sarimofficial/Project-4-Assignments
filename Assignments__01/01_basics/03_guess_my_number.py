import random

def guess_my_number():
    secret_number = random.randint(0, 99)
    max_attempts = 7
    attempts = 0
    
    print(f"I'm thinking of a number between 0 and 99 (you have {max_attempts} tries)")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts}: "))
            
            if guess == secret_number:
                print(f"🎉 Correct! The number was {secret_number}")
                return
            elif guess < secret_number:
                print("⬆️ Too low")
            else:
                print("⬇️ Too high")
                
            attempts += 1
        except ValueError:
            print("❌ Please enter a valid number")
    
    print(f"Game over! The number was {secret_number}")

guess_my_number()