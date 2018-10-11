import datetime

myname = '<ravi teja>'
myid = '<ncd0918h007>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

ten_things = "apples oranges crows telphone light sugar"

print " wait there is not 10 thngs int hat list let fix it"

stuff = ten_things.split(' ')
more_stuff =["day"," ni8","song","fris", "corn", " ban", "girl", "boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print "adding: ", next_one
    stuff.append(next_one)
    print " there is %d items now" % len(stuff)

print "there we go" , stuff

print " lets do sme thngs "

print stuff[1]
print stuff[-1]
print ''.join(stuff)
print'#'.join(stuff[3:5])