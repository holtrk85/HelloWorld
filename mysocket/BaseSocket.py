import socket

class BaseSocket:
  def __init__( self, localIP, localPort, bufferSize ):
    self.localIP     = localIP
    self.localPort   = localPort
    self.bufferSize  = bufferSize

  def start( self ):
    msgFromServer       = "Hello UDP Client"
    bytesToSend         = str.encode(msgFromServer)

    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((self.localIP, self.localPort))

    print("UDP server up and listening on " + self.localIP + ":" + str(self.localPort))

    # Listen for incoming datagrams
    while(True):
      bytesAddressPair = UDPServerSocket.recvfrom(self.bufferSize)
      message = bytesAddressPair[0]
      address = bytesAddressPair[1]
    
      clientMsg = "Message from Client:{}".format(message)
      clientIP  = "Client IP Address:{}".format(address)
    
      print(clientMsg)
      print(clientIP)

      # Sending a reply to client
      UDPServerSocket.sendto(bytesToSend, address)