class Utilities:

  @staticmethod
  def get_int_input(prompt):
    choice = None
    while True:
      try:
        choice = int(input(prompt))
        return choice
      except:
        print("Thats not an allowed choice.")

  @staticmethod
  def get_str_input(prompt):
    word_input = None
    while True:
      word_input = input(prompt)
      if word_input.isalpha():
        return word_input
      else:
        print("Only letters allowed in words.")