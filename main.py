import random
import hangman_art
import hangman_words

list_words = hangman_words.words
chosen_word = random.choice(list_words)
word_characters = list(chosen_word)
hangmanpics = hangman_art.HANGMANPICS
blanks =[]
length_word = len(chosen_word)
for i in range (length_word):
    blanks.append("_")
total_lives = 6
lives_lost = 0
print(hangman_art.logo)
while (lives_lost <= 6 and "_" in list(blanks)):
    print(f"\n{blanks}")
    input_letter = input("\nGuess the letter ").lower()
    if (input_letter not in word_characters):
        print(hangmanpics[lives_lost])
        lives_lost = lives_lost + 1   
    else:
        for i in range(len(word_characters)):
            if (input_letter == word_characters[i]):
                blanks[i] = input_letter
    if(lives_lost == 6):
        print(hangmanpics[6])
        print(hangman_art.game_over)
        print(f"The word was {chosen_word}")
        exit()
    if("_" not in list(blanks)):
        print(hangman_art.you_win)
        print(f"The word was {chosen_word}")
        









    



