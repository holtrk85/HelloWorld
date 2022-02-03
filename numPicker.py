import random

class NumPicker:
  def secret(self):
    secret_number = str(random.randint(1,5))
    print("Pick a number between 1 to 5 ")
    while True:
      res = input("Guess the number: ")
      if res==secret_number:
        print("You win")
        break
      else:
        print ("You lose")
        continue