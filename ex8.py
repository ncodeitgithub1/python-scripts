import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
formatter="%r %r %r"
print formatter %(1,2,3)
print formatter %("one","two","three")
print formatter %(True,False,True)
print formatter %(
"ihad this thing",
"that u coould sing",
"but it didnt sing"
)
