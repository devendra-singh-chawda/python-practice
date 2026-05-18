import random
print(" Welcome to Number Guessing Game ")
print(" Made by Devendra Singh Chawda ")

print("\nSelect Difficulty Level")
print("1. Easy   (1 to 50)")
print("2. Medium (1 to 100)")
print("3. Hard   (1 to 500)")

choice = input("Enter your choice: ")

if choice == "1":
    max_number = 50
    difficulty = "Easy"

elif choice == "2":
    max_number = 100
    difficulty = "Medium"

elif choice == "3":
    max_number = 500
    difficulty = "Hard"

else:
    print("Invalid choice")
    exit()

secret_number = random.randint(1, max_number)

print("\nYou selected", difficulty, "mode")
print("I have selected a number between 1 and", max_number)

guess = 0
attempts = 0

while guess != secret_number:

    guess = int(input("\nEnter your guess: "))

    attempts = attempts + 1

    if guess == secret_number:
        print("Correct guess!")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Too high")

print("\nYou guessed the number in", attempts, "attempts")
print("Game Over")