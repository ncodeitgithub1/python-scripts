import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()                  
tabby_cat="\t am tabbed in"
persian_cat="am split\non a line"
backslash_cat="am \\ a \\ cat"
fat_cat="""
i will do a list:
\t* cat food 
\t * fishies
\t * catnip\n\t* grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

