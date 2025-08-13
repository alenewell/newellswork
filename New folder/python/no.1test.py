import random
secret_number = random.randint(1, 20)
max_attempts = 5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")
print(f"You have {max_attempts} chances to guess it.")
for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}: Take a guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Good job! You guessed my number in {attempt} tries!")
        break
else:
    print(f"Sorry, you've used all your attempts. The number was {secret_number}.")