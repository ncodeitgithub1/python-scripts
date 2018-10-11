ten_things="apples oranges crows telephone light sugar"
print "wait there's not 10 things in that list, lets fix that"
stuff=ten_things.split(' ')
more_stuff=["day","nyt","song","frisbee","corn","banana","girl","boy"]
while len(stuff)!=10:
   next_one=more_stuff.pop()
   print "adding:", next_one
   stuff.append(next_one)
   print "ther is %d items now" %len(stuff)
print "there we go:", stuff
print "lets do sum things"
print stuff[1]
print stuff[-1]
print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:5])
