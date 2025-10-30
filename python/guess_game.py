import random

# توليد رقم عشوائي بين 1 و 100
answer = random.randint(1, 100)
user_wins = False
attempts = 0

while not user_wins:
    guess = input("Enter a number between 1 and 100: ")

    # نحاول نحول الإدخال لرقم
    try:
        guess_number = int(guess)
    except:
        print("Error: you need to enter a valid number.")
        quit()

    # نزود عدد المحاولات بعد التأكد إن الإدخال صحيح
    attempts += 1

    # نبدأ المقارنة
    if guess_number == answer:
        user_wins = True
    elif guess_number > answer:
        print("The secret number is smaller.")
    else:
        print("The secret number is bigger.")

# بعد الفوز نختار كلمة مفرد أو جمع
if attempts == 1:
    attempt_word = "attempt"
else:
    attempt_word = "attempts"

print(" You win!! You took " + str(attempts) + " " + attempt_word + ".")

                 