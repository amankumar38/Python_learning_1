word_to_guess = "Sultan"
guess = ""
guess_count = 0
guess_count_limit = 5
out_of_guess = False

while guess != word_to_guess and not (out_of_guess):
    if guess_count < guess_count_limit:
        guess = input("Enter the secret word\n")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of limit! You Lose..")
else:
    print("Hurray..You Won..")
