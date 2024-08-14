import random

print("\tWelcome to code-breaker game!\n\nI guessed a 3 digit number, can you guess it?")


# Function created for generate 3 digits number, number start with 1 to 9 not 0
def generate_number(li):
    while True:
        x = random.sample(li, 3)
        if x[0] != 0:
            return x


# Function created for user accept number guess with sys secret number
def guessing_number(secret_number):
    while True:
        # Only 3 digits accept , input character not allow
        try:
            user_number = [int(i) for i in input("\nEnter your guess:")]
            if len(user_number) != 3:
                print("Oops Wrong Input!\n\n* Please Enter 3 digits number ")
                continue
        except:
            print("Oops Wrong Input!\n\n* Please Enter 3 digits number \n* character not accepted")
            continue

        if user_number == secret_number:
            print("Matched! You are a code-breaker!")
            break

        result = ""

        for i in range(len(user_number)):
            if user_number[i] == secret_number[i]:
                result += str(user_number[i])
            else:
                result += "X"

        if result == "XXX":
            print("Sorry no match! Try again, Enter your guess\n")
        else:
            print(f"Close [{result}] ! Try again, Enter your guess\n")


guessing_number(generate_number(range(0, 9)))

# number_range=range(0,9)
# secret_number = generate_number(number_range)
# guessing_number(secret_number)
