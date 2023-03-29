# user keeps typing in secret word until they get it right

secret_word = "giraffe"
guess = "" # store users guess
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    print(guess)
    if guess_count < guess_limit:
      guess = input("Enter guess: ")
      guess_count += 1
    else:
      out_of_guesses = True

if out_of_guesses:
  print("Out of Guesses, YOU LOSE!")
else:
  print("You win")