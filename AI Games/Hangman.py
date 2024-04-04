import random

name = input("What is your name? ")
print("Good Luck! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
print("Guess the characters")

# Initialize 'guesses' as an empty list, not an empty string
guesses = []

# Set 'turns' to 12 as per your original code
turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\n\nYou Win!!")
        print("The word is:", word)
        break

    print("\n")

    guess = input("Guess a character: ")

    if len(guess) != 1:
        print("Please enter a single character!")
        continue

    guesses.append(guess)

    if guess not in word:
        turns -= 1
        print("Wrong!!")
        print("You have", turns, 'more guesses!')

    if turns == 0:
        print("\nYou Lose!!")
        print("The word was:", word)
