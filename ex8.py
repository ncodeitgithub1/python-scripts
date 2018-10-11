import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one","Two","Three","Four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
    "I had this thing.",
    "that you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)