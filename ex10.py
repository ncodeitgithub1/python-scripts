import datetime
myname = 'jeethendar'
myid = 'NCD0818H007'
now = datetime.datetime.now()

print  "Script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "--------------------------------------------------------"



tabby_cat = "\tI'm tabbled in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
Ill do a list:
\t* Cat food
\t* Fishes
\t Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

