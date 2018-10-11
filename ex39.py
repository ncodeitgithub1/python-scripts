import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
states=[
    'Oregon':'OR',
    'florida':'FL',
    'california':'CA',
    'Newyork':'NY',
    'micihgan':'MI'
]
cities=[
     'CA':'San fransisco',
     'MI':'Detroit',
     'FL':'Jacksonvile'
]
cities['NY']='Newyork'
cities['OR']='portland'
print '-'*10
print "NY state has:", cities['NY']
print "OR state has:", cities['OR']
print '-'*10
print "Michigan has", cities[states['Michigan']]
print "Florida has", cities[states['Florida']]
print '-'*10
for state ,abbrev in states.items():
    print "%s is abbreviated %s" %(state,abbrev)
print '-'*10
for abbrev,city in cities.items():
    print "%s has the city %s" %(abbrev,city)
print '-'*10
for state,abbrev in states.items():
     print "%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev])
print '-'*10
state=states.get('texas',None)
if not state:
print "sorry,no texas"
city=cities.get('TX', 'does not exist')
print "the city for the state 'TX' is : %s" %city

