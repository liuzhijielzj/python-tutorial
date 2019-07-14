class MyTCPServer(TCPServer, ForkingMixIn):
    pass

class MyTCPServer(TCPServer, CoroutineMixIn):
    pass

class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
