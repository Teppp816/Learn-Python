# The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.

# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

# Magic 8-Ball, should I do this project?

# We’ll be using the following 9 possible answers for our Magic 8-Ball:

# Yes - definitely
# It is decidedly so
# Without a doubt
# Reply hazy, try again
# Ask again later
# Better not tell you now
# My sources say no
# Outlook not so good
# Very doubtful

import random
random_number = random.randint(1, 9)

name = "Luan"
question = "Am I cute?"
answer = ""

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say so"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

if name == "":
  print("Question: ", question)
else:
  print(name, " asks: ", question)

if question == "":
  print("Please ask a question.")
else:
  print("Magic 8-Ball's answer: ", answer)
# print(random_number)