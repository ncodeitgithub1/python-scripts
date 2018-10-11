import datetime
myname = 'vasantha'
myid =  'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print '_' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']
print '_' * 10
print "michigan's abbrevation is: ", states['Michigan']
print "florida's abbrevation is: ", states['Florida']
print '_' * 10
print "michigan has: ", cities[states['Michigan']]
print "florida has: ", cities[states['Florida']]
print '_' * 10
for state, abbrev in states.items():
    print "%s is abbrevated as %s" % (state, abbrev)
print '_' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
print '_' * 10
for state, abbrev in states.items():
    print "%s state is abbrevated %s and has city %s" % (
        state, abbrev, cities[abbrev])
print '_' * 10
state = states.get('texas', None)
if not state:
    print "sorry. no texas."
city = cities.get('TX', 'does not exist')
print "the city for the state 'TX' is: %s" % city

