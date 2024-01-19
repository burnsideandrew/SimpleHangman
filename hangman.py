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

# def match_with_gaps(my_word, other_word):
#     '''
#     my_word: string with _ characters, current guess of secret word
#     other_word: string, regular English word
#     returns: boolean, True if all the actual letters of my_word match the 
#         corresponding letters of other_word, or the letter is the special symbol
#         _ , and my_word and other_word are of the same length;
#         False otherwise: 
#     '''
#     # FILL IN YOUR CODE HERE AND DELETE "pass"
#     pass



# def show_possible_matches(my_word):
#     '''
#     my_word: string with _ characters, current guess of secret word
#     returns: nothing, but should print out every word in wordlist that matches my_word
#              Keep in mind that in hangman when a letter is guessed, all the positions
#              at which that letter occurs in the secret word are revealed.
#              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
#              that has already been revealed.

#     '''
#     # FILL IN YOUR CODE HERE AND DELETE "pass"
#     pass



# def hangman_with_hints(secret_word):
#     '''
#     secret_word: string, the secret word to guess.
    
#     Starts up an interactive game of Hangman.
    
#     * At the start of the game, let the user know how many 
#       letters the secret_word contains and how many guesses s/he starts with.
      
#     * The user should start with 6 guesses
    
#     * Before each round, you should display to the user how many guesses
#       s/he has left and the letters that the user has not yet guessed.
    
#     * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
#     * The user should receive feedback immediately after each guess 
#       about whether their guess appears in the computer's word.

#     * After each guess, you should display to the user the 
#       partially guessed word so far.
      
#     * If the guess is the symbol *, print out all words in wordlist that
#       matches the current guessed word. 
    
#     Follows the other limitations detailed in the problem write-up.
#     '''
#     # FILL IN YOUR CODE HERE AND DELETE "pass"
#     pass

if __name__ == "__main__":
    pass
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
