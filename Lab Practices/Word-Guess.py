import random

word_bank = ["amazing", "lovely", "enthusiasm", "smart", "beautiful"]

word = random.choice(word_bank)
#random.choice() method is used to randomly select a word from the word_bank

guessedWord = ['_'] * len(word)

attempts = 10

while attempts > 0:
    print('\nCurrent Word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ')
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
        if '_' not in guessedWord:
            print('\nCongratulations!! You guessed the word: ' + word)
            break
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
        if attempts < 1:
            print('\nYou\'ve run out of attempts! The word was: ' + word)
            break

