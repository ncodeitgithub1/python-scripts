import datetime
myname = '<ravi teja>'
myid = '<ncd0918h007>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

states = {
    'Oregon': 'OR',
    'florida': 'FL',
    'california':'CA',
    'new york': 'NY',
    'michigan': 'MI'
}

cities = {
    'CA' : 'san fransco',
    'MI' : 'detroit',
    'FL' :'jacksonville'
}

cities['NY'] = ' new york'
cities['OR'] = 'portland'
print '-' * 10
print "NY state has:" ,cities['NY']
print "OR state has:" ,cities['OR']

print '-' * 10
print " michigan has:", cities[states['michigan']]
print "florida has:", cities[states['florida']]

print '- ' * 10
print "michigan has: ", cities[states['michigan']]
print "florida has: ", cities[states['florida']]

print '- ' * 10
for state, abbrev in states.items():
    print " %s is abbreviated %s " % (state, abbrev)

print '- ' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '- ' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
print '- ' * 10
state = states.get('texas', None)
if not state:
    print "Sorry, no Texas."

city = cities.get('TX', 'Does Not Exist')
print "the city of the state 'TX' is: %s" % city


