import random

print("🌸 Welcome to the Cute Guessing Game! 🌸")
print("I am thinking of a number between 1 and 20...")

secret_number = random.randint(1, 20)
attempts = 0

while True:
    try:
        guess = int(input("💖 Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again cutie 💕")
        elif guess > secret_number:
            print("📈 Too high! Try again sweetheart 💗")
        else:
            print(f"🎉 Yay!! You got it in {attempts} tries 💐")
            print("✨ You are amazing! Thanks for playing 🌈")
            break

    except ValueError:
        print("😅 Please enter a valid number!")