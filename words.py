class Word:
  def __init__(self, swedish_word, english_word):
    self.__swedish_word = swedish_word.lower()
    self.__english_word = english_word.lower()

  def get_swedish_word(self):
    return self.__swedish_word

  def get_english_word(self):
    return self.__english_word

  def verify_answer(self, english_guess):
    return self.__english_word == english_guess.lower()

  def to_string(self):
    return f"({self.__swedish_word}, {self.__english_word})"