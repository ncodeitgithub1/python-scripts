import datetime
myname = 'shiva'
myid = 'NCD0518H028'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The word is saved"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people > dogs:
    print "People are greated than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs"

if people == dogs:
    print "People are dogs"

    

