ten_things = "Apples oranges crows telephone light sugar"
print "Wait there's not 10 things in that list, let's fix that."
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night","Song","Frisbee","Corn", "banana", "girl", "boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "These's %d items now." % len(stuff)
print "There we go: ", stuff
print "Let's ddo some things with stuff."
print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
