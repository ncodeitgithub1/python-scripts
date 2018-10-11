import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
tabby_cat = "\t i'm tabbed in."
persian_cat = "i'm split\not a line"
black_cat = "i'm \\ a \\ cat"
fat_cat = """
i'll do  a list:
\t* cat food
\t* fishes
"""
print tabby_cat
print persian_cat
print black_cat
print fat_cat
