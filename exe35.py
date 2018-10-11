import datetime
myname = '<kavya>'
myid = '<NCD0918H006>'
now = datetime.datetime.now()

print" script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import exit
def gold_room():
    print "this room is full of gold. how much do you take?"
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("man, learn to type a number")
    if how_much < 50:
        print "nice, you are not greedy"
        exit(0)
    else:
        dead("you greedy bastard!")
def bear_room():
    print "there is abear"
    print "the bear has a"
    print "the fat bear is in front of another door"
    print "how are you going"
    bear_moved = False
    while True:
        next = raw_input("> ")
        if next == "take honey":
            dead("the bear looks at you then slaps")
        elif next == "taunt bear" and not bear_moved:
            print "the bear has moved from the door."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("the bear gets prissed off")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "i got no idea"
def cthulhu_room():
    print "here you see the great evil"
    print "he it whatever"
    print "do you flee for your life or eat your head?"
    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        cthulhu_room()
def dead(why):
    print why, "good job"
    exit()
def start():
    print "you are in adark room"
    print "there is adoor to your right and left"
    print "which one do you take?"
    next = raw_input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("you stumble around the room until you starve")
start()
