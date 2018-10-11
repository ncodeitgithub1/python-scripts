import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
states = {
    'Oregon': 'OR',
    'Florida' : 'FL',
    'California': 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA' : 'SAn Fansisco',
    'MI' : 'Detroit',
    'FL':'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print '_' * 10
print "NY States has: ",cities['NY']
print "OR State has:" , cities['OR']

print '_' * 10
print "Michigan's abbrevation is :",states['Michigan']
print "Florida has: ", states['Florida']

print '_' * 10
for state, abbrev in states.items():
    print "%s is abbrevated %s" % (state,abbrev)
print '_' * 10
for abbrev,city in cities.items():
    print "%s hhas the city %s" % (abbrev, city)
print '_' * 10
for state, abbrev in states.items():
    print "%s state is abbrevated %s and has city %s" % (state,abbrev,cities[abbrev])
print '_' * 10
state = states.get('Texas', None)
if not state:
    print "SOrry, no Texas."
city = cities.get('TX', 'Does Not exist')
print "The city for the state 'TX' is: %s" % city
