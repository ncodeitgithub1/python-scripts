import datetime
myname = '<kavya>'
myid = '<NCD0918H006>'
now = datetime.datetime.now()

print" script executed by %s with id %s " % (myname, myid)
print now.isoformat()
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}



cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}


cities['NY'] = 'New York'
cities['OR'] = 'Portland'


print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']


print '-' * 10
print "Michigan's abbreviation is : ", states['Michigan']
print "Florida's addreviation is: ", states['Florida']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]


print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)


print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)


print "-" * 10
for stae,abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
    state,abbrev,cities[abbrev])

print '-' * 10

state = states.get("Texas")

if not state:
    print "sorry, no Texas"
city = cities.get('tx', 'Does Not Exist')
print "the city for thr state 'TX' is: %s" % city


city = cities.get('TX', 'Does not Exist')
print "the city for the state 'Tx' is : %s" % city