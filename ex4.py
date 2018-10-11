import datetime
myname = 'Avinash'
myid = 'NCD0318H022'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
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
print "we can transport", "to carpool today"
print "we nese t put about",
average_passengers_per_car, "in each car"
