from sys import exit

def monster_room():
    print "You have run into a monster room."
    print "The monster is sleeping in front of another door."
    print "How you get through of that door?"
    while True:
        next = raw_input("> ")
        
        if next == "use fire":
            dead("The monster wakes up, and eats you.")
        elif next == "fight with it":
            dead("The monster wakes up, and eats you.")
        elif next == "play music":
            gold_room()
        else:
            print "I have no idea what that means."

            
def mermaid_room():
    print "You have run into a mermaid room."
    print "You see a beautiful lady
