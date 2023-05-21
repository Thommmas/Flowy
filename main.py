from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.protocols import basic

class BitTorrentProtocol(Protocol):
    def connectionMade(self):
        print("Connected to peer")

    def connectionLost(self, reason):
        print("Connection lost:", reason)

    def dataReceived(self, data):
        # Process received data
        print("Received data:", data)

class BitTorrentClientFactory(ClientFactory):
    protocol = BitTorrentProtocol

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed:", reason)
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost:", reason)
        reactor.stop()

if __name__ == "__main__":
    endpoint = TCP4ClientEndpoint(reactor, "127.0.0.1", 6881)  # Replace with actual peer IP and port
    factory = BitTorrentClientFactory()
    endpoint.connect(factory)
    reactor.run()
