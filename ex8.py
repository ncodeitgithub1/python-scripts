import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "Four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing",
    "That you could type up right.",
    "But it didn't sing",
    "SO I said goodnight ")
