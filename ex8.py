import datetime
myname = 'MD SABAIR'
myid = 'NCD0318H018'
now = datetime.datetime.now()

formatter="%r %r %r"
print formatter %(1,2,3)
print formatter %("one","two","three")
print formatter %(True,False,True)
print formatter %(
"ihad this thing",
"that u coould sing",
"but it didnt sing"
)
