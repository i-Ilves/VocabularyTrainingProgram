from utilities import Utilities
from words import Word
from topscores import Topscore
from random import shuffle

class VocabularyTraningProgram:
  max_failures = 3
  topscore = Topscore()
  words = [
    Word("mytisk", "mythical"),
    Word("organism", "organism"),
    Word("osofistikerad", "unsophisticated"),
    Word("genomföra(implementera)", "implement"),
    Word("förberedelse", "preparation"),
    Word("humoristisk", "humorous"),
    Word("undantagsvis", "exceptionally"),
    Word("bojor", "shackles"),
    Word("informell", "informal"),
    Word("gurglande", "gurgling"),
    Word("medvetande", "consiousness")
  ]


  def menu_switcher(self, choice):
    switch = {
      "1": self.add_new_word,
      "2": self.shuffle_words,
      "3": self.take_the_test,
      "4": self.show_all_the_words,
      "5": self.topscore.show_topscore_list
    }
    return switch[choice]

  def show_menu(self):
    choice = None
    while choice != 6:
      print(
        '''
        1. Add a new word
        2. Shuffle the word list
        3. Start the test
        4. Show the word list
        5. Show TopScore list
        6. Exit
        '''
      )

      choice = Utilities.get_int_input("Enter your menu choice: ")

      if choice < 1 or choice > 6:
        print("Thats not a valid menu choice.")
      elif choice != 6:
        self.menu_switcher(str(choice))()
      else:
        self.exit_game()

  def add_new_word(self):
    swedish_word = Utilities.get_str_input("Enter word in Swedish: ")
    english_word = Utilities.get_str_input("Enter the corresponding word in English: ")
    self.words.append(Word(swedish_word, english_word))
    print()
    print("Added the new word.")

  def take_the_test(self):
    points = 0
    misses = 0
    for word in self.words:
      print()
      answer = input(f"What is the English translation for {word.get_swedish_word()}? ")
      if word.verify_answer(answer):
        points += len(answer)
        print("Correct!")
      else:
        misses += 1
        print(f"Wrong! The correct answer is {word.get_english_word()}.")
        if misses == self.max_failures:
          print()
          print("GAME OVER! You need more practise!")
          return
    print(f"The test is over. You got {points} points.")
    if self.topscore.qualify_for_topscore(points):
      print()
      print("Congrats! You got in on the TopScore list!")
      name = Utilities.get_str_input("What is you name? ")
      self.topscore.append_to_topscore([name, str(points)])
      print("Your score has been added to the TopScore list.")
    else:
      print()
      print("You did not get in on the TopScore list. Better luck next time.")

  def exit_game(self):
    print("Game closing...")

  def shuffle_words(self):
    shuffle(self.words)
    print("The wordlist has been shuffled!")

  def show_all_the_words(self):
    for word in self.words:
      print(word.to_string())

 