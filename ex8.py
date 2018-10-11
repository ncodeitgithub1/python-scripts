import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()






formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter %("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)

print formatter % (
                 "i had this thing",
                  "that you could type upright",
                   "but it didnt sing",
                   "so i said good night")
