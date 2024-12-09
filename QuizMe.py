print("Welcome to the quiz")

playing = input("Want to play? ")
if playing.lower() != "yes":
    quit('Later')
print("Let's play: ")
score = 0

answer = input("What is 10 * 10? ")
if answer == '100':
    print("Correct!")
    score += 1
else:
    print("Wrong, yikes...")

answer = input("What is 7 * 7? ")
if answer == '49':
    print("Correct!")
    score += 1
else:
    print("Wrong, yikes...")

answer = input("What is 2 * 36? ")
if answer == '72':
    print("Correct!")
    score += 1
else:
    print("Wrong, yikes...")

answer = input("What is 9 * 11? ")
if answer == '99':
    print("Correct!")
    score += 1
else:
    print("Wrong, yikes...")

print("Final score of correct answers: " + str((score/4) * 100) + "%")
