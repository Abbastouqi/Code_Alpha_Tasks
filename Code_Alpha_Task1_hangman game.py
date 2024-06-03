#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random


# # Define the list of words
# 
# 
# 

# In[12]:


import random

# Step 2: Get the list of words from user input
def get_words():
    words_input = input("Enter words separated by spaces: ")
    words = words_input.split()
    return words

# Step 3: Define the function to choose a random word
def choose_word(words):
    return random.choice(words)

# Step 4: Define the function to display the current state of the word without list comprehension
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

# Step 5: Define the main game function
def hangman_game():
    words = get_words()  # Get words from user input
    word = choose_word(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nCurrent word: {display_word(word, guessed_letters)}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} tries left.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

# Run the game
hangman_game()


# In[ ]:





# In[ ]:





# In[ ]:




