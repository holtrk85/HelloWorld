import time

class TestThread():

  def __init__(self, num):
    self.num = num

  def body(self):
    print("Thread %s: starting" % self.num)
    time.sleep(self.num)
    print("Thread %s: finishing" % self.num)