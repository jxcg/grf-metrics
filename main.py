import prometheus_client
from scapy.all import *

class NetworkClient:
    def __init__(self):
        pass

    def packet_handler(self, packet):
        print(packet.summary())


class PromClient:
    def __init__(self):
        pass


if __name__ == "__main__":
    print("app started")
    pc = PromClient()
    nc = NetworkClient()
    sniff(prn=nc.packet_handler, count=10)
