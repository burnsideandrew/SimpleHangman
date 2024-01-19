import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():

    print("Loading word list from file...")

    inFile = open(WORDLIST_FILENAME, 'r')

    line = inFile.readline()

    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
       if char not in letters_guessed:
          return False
       
    return True

def get_guessed_word(secret_word, letters_guessed):
    iterated_word = ''
    for char in secret_word:
       if char not in letters_guessed:
          iterated_word += ' _ '
       else:
          iterated_word += char

    return iterated_word

def get_available_letters(letters_guessed):
    chars_left = list(string.ascii_lowercase)
    for char in letters_guessed:
       if char in string.ascii_lowercase:
          chars_left.remove(char)

    return chars_left
          

    

def hangman(secret_word):
    guess_count = 6
    letters_guessed = []
    warning_count = 0
    print('Welcome to the game Hangman!\n')
    print('I am thinking of a word with', len(secret_word), 'letters.\n----------------')
    
    while guess_count > 0 and warning_count < 3:
      print('You have', guess_count, 'guesses left.\n')
      print('Please type your guess as a lower-case letter and press enter/return:')
      user_guess = input()

      if user_guess in string.ascii_lowercase:
          if user_guess not in letters_guessed:
            letters_guessed.append(user_guess)
          else:
            warning_count += 1
            print('Letter already guessed. Warning count:', warning_count)
            continue
          if is_word_guessed(secret_word, letters_guessed) == True:
            print('You won!', 'Word:', secret_word, 'Guesses left:', guess_count)
            quit()
      else:
        if len(user_guess) >= 2:
          if user_guess == secret_word:
            print('You won!', 'Word:', secret_word, 'Guesses:', guess_count)
            quit()
          elif len(user_guess) >= 2:
             if user_guess != secret_word:
              print('Wrong word. Please try again.')
          else:
            if user_guess not in string.ascii_lowercase:
              warning_count += 1
              print('\nYou did not enter a letter. Please try again. Warning Count:', warning_count, '\n')
              continue

      guess_count -= 1
      get_guessed_word (secret_word, letters_guessed)

      if user_guess not in secret_word:
        print('\nBad guess.', user_guess, 'is not in my word.\n')
      else:
        print ('\nGood guess!', user_guess, 'is in my word.')

      print('\nGuesses left: ', guess_count, '\n Available letters:', get_available_letters(letters_guessed), '\n', get_guessed_word(secret_word, letters_guessed), '\n')
        
    print ('You lost! No more guesses left.')
    print ('The secret word was:', secret_word)



if __name__ == "__main__":
    pass
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
