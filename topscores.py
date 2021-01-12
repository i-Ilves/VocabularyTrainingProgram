class Topscore:
  def __init__(self):
    self.topscore_list = self.get_topscore_as_list()
    # print(self.topscore_list)

  def get_topscore_as_list(self):
    topscores = open("topscores.txt")
    topscores_list = topscores.readlines()
    topscores.close()
    if topscores_list:
      topscores_list = [x.replace("\n", "") for x in topscores_list]
      topscores_list = [x.split(" - ") for x in topscores_list]
      topscores_list.sort(reverse=True, key=lambda x: x[1])
      return topscores_list
    else:
      return []

  def append_to_topscore(self, score):
    topscore = open("topscores.txt", "a")
    score_str = " - ".join(score)
    topscore.write(f"{score_str}\n")
    topscore.close()
    self.topscore_list = self.get_topscore_as_list()

  def show_topscore_list(self):
    self.get_topscore_as_list()
    if self.topscore_list:
      print()
      print(self.topscore_list)
    else:
      print()
      print("The TopScore list is empty.")
      
  def write_over_topscore(self):
    topscore = open("topscores.txt", "w")
    for h in self.topscore_list:
      score_str = " - ".join(h)
      topscore.write(f"{score_str}\n")
    self.topscore_list = self.get_topscore_as_list()

  def get_lowest_score(self):
    lowest = None
    for h in self.topscore_list:
      if not lowest:
        lowest = int(h[1])
      else:
        if lowest > int(h[1]):
          lowest = int(h[1])
    return lowest

  def qualify_for_topscore(self, points):
    if len(self.topscore_list) == 5:
      if points > self.get_lowest_score():
        self.topscore_list.pop(-1)
        self.write_over_topscore()
        return True
    else:
      return True
    return False


