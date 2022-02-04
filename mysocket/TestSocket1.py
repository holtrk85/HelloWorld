from mysocket import BaseSocket

class TestSocket1(BaseSocket.BaseSocket):
  def __init__( self ):
    BaseSocket.BaseSocket.__init__(self,"127.0.0.1",20001,1024)

