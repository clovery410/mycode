cars = 100 #assign variable cars equals to 100
space_in_a_car = 4.0 #assign variable space_in_a_car equals to 4.0, it is a floating number
drivers = 30 #assign variable drivers equals to 30
passengers = 90 #assign variable passengers equals to 90
cars_not_driven = cars - drivers #assign variable car_not_driven equals to cars minus drivers
cars_driven = drivers #assign variable cars_driven equals to variable drivers
carpool_capacity = cars_driven * space_in_a_car #assign variable carpool_capacity equals to cars_driven multiple by space_in_a_car
average_passengers_per_car = passengers / cars_driven #assign variable average_passengers_per_car equals to passengers divided by cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."