import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be ", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "peole today"
print "web have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"
