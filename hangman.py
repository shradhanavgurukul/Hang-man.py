import  string
from words import choose_word
from images import IMAGES

def ifvalid(user_input):
  if len(user_input)!=1:
    return False
    if not user_input.isalpha():
      return False
    return True

def is_word_guessed(secret_word, letters_guessed):
    if secret_word==get_guessed_word(secret_word,letters_guessed):
      return True
    return False
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):
    import string
    letters_left = string.ascii_lowercase
    letters_left=""
    for i in letters_guessed:
          if i not in letters_guessed:
            letters_left=letters_left.replace(i,"")
            letters_left+=i
    return letters_left
def get_hint(secret_word,letters_guessed):
  import random
  letters_not_guessed=[]
  i=0
  while i<len(secret_word):
    if i not in letters_guessed:
      if i not in letters_not_guessed:
        letters_not_guessed.append(i)
      i=i+1
  return random.choice(letters_not_guessed)
def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("")
    letters_guessed = []
    total_lives=remaining_lives=8
    image_selection_list_indices=[0,1,2,3,4,5,6,7]
    user_difficultiy_choice=input("Aap abhi kitni difficulty par yeh game khelna chahte ho?\na)\tEasy\nb)\tMedium\nc)\tHard\n\nApni choice a, b, ya c ki terms mei batayein\n")
    if user_difficultiy_choice not in ["a","b","c"]:
        print("Aapki choice invalid hai.\nGame easy mode mei start kar rahe hai")
    else:
      if user_difficultiy_choice=="b":
        total_lives=remaining_lives=6
        image_selection_list_indices=[1,2,3,4,5,6,7]
      elif user_difficultiy_choice=="c":
        total_lives=remaining_lives=4
        image_selection_list_indices=[1,3,5,7]
      else:
        if user_difficultiy_choice=="a":
          total_lives=remaining_lives=6
          image_selection_list_indices=[1,2,3,4,5,6,7]
          print("your choice is in valid""\n""game is starting in easy level")
      while (remaining_lives>0):
            available_letters=get_available_letters(letters_guessed)
            print("Avaliable letters: "+available_letters)
            guess=input("please guess a letter: ")
        # if guess=="hint":
          # print(("your hint for this secret word is:"+get_hint(secret_word,letters_guessed)))
        # letter=get_hint(secret_word,letters_guessed)
            letter=guess.lower()
            if(not ifvalid(letter)):
              pass
          # continue
        # if guess=="hint":
              # print("your hint for this secret word is:"+get_hint(secret_word,letters_guessed))
            if letter in secret_word:
              letters_guessed.append(letter)
              print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
              print("")
              if is_word_guessed(secret_word, letters_guessed) == False:
                print("😄😄good guess😄😄")
                # print(" * *😄😄Congratulations, you won!😄😄 * * ")
                print("")
                # break
        # continue
              else:
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                letters_guessed.append(letter)
                print(IMAGES[8-remaining_lives])
                remaining_lives-=1
                print("Remaning LIVE:"+str(remaining_lives))
                print("")
          
          # continue
            else:
              print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
              letters_guessed.append(letter)
              print(IMAGES[8-remaining_lives])
              remaining_lives-=1
              print("Remaning LIVE:"+str(remaining_lives))
              print("") 
      else:
        print("🙁🙁sorry,you lose the game🙁🙁,the word was"+str(secret_word)+".")       
secret_word = choose_word()
hangman(secret_word)