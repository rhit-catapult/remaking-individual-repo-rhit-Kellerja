import random
print("guess my number")

secret_number = random.randint(1, 100)
# print(secret_number) #to do: remove
counter = 0

while True:
    guess = int(input("guess a number: "))
    print(guess)
    counter += 1
    if guess > secret_number:
        print("too high")
    if guess < secret_number:
        print("too low")
    if guess == secret_number:
        print("you win")
        break

print(f"You got it in {counter} guesses.")
# Pseudocode

# establish variable of counter set zero

# select secret number 1-100

# start loop
# prompt usser
# save guess
# if too high display
# if too low display
# if correct display and end loop

#tell usser how many guess
