import random

class NumPicker:

  def __init__(self, max):
    self.max = max

  def secret(self):
    secret_number = str(random.randint(1, self.max))
    print("Pick a number between 1 to " + str(self.max))
    while True:
      res = input("Guess the number: ")
      if res==secret_number:
        print("You win")
        break
      else:
        print ("You lose")
        continue