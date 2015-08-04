class Email(object):
    """Every email object has 3 instance variables: the message, the sender(their name), and the addressee(the destination's name)."""
    def __init__(self, msg, sender, addressee):
        self.msg = msg
        self.sender = sender
        self.addressee = addressee

class Postman(object):
    """Each Postman has an instance variable clients, which is a dictionary that associates client names with client objects."""
    def __init__(self):
        self.clients = dict()

    def send(self, email):
        """Take an email and put it in the inbox of the client it is addressed to."""
        client = self.clients[email.addressee]
        client.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it to the clients instance variable."""
        self.clients[client_name] = client

class Client(object):
    """Every Client has instance varibales name(which is used for addressing emails to the client), mailman(which is used to send emails out to other clients), and inbox(a list of all emails the client has received).
    """
    def __init__(self, mailman, name):
        self.inbox = list()
        self.mailman = mailman
        self.name = name
        self.mailman.register_client(self, self.name)

    def compose(self, msg, recipient):
        """Send an email with given message msg to the given recipient."""
        email = Email(msg, self, recipient)
        self.mailman.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        self.inbox += email


if __name__ == '__main__':
    post1 = Postman()
    c1 = Client('Clover','client1' )
    post1.register_client(c1, "AAA")
    print(post1.clients)
    
