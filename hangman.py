import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear

end_game = False
#total hangman lives are 6 so
lives = 6

print(logo)
random_word = random.choice(word_list)
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

display = []
word_length = len(random_word)
i = 0
while i < word_length:
    display.append("_")
    i += 1
print(display)

while not end_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}.")
    for position in range(word_length):
        letter = random_word[position]
        if guess == letter:
            display[position] = letter
    # Check if user is wrong.
    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.")
    # Join all the elements in the list and turn it into a String.
    print(f"{''.join(display)}")
    # Check if user has got all letters.
    if "_" not in display:
        end_game = True
        print("You Win")

    print(stages[lives])