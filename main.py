from mygames import NumPicker
from mysocket import TestSocket1
from mythread import TestThread
import sys
import threading

print("Version = ", sys.version_info)

for tNum in range(10):
  newThread = TestThread.TestThread( tNum )
  t = threading.Thread(target=newThread.body)
  t.start()

np = NumPicker.NumPicker( 2 )
np.secret()
print( "DONE")
ts = TestSocket1.TestSocket1()
ts.start()