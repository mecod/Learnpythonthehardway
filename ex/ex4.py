# 车辆数目
cars = 100
# 汽车承载能力
space_in_a_car = 4.0
# 司机数量
drivers = 30
# 乘客数量
passengers = 90
# 没有司机的汽车数
cars_not_driven = cars - drivers
# 有司机的汽车数
cars_driven = drivers
# 总的汽车承载能力
carpool_capacity = cars_driven * space_in_a_car
# 每辆汽车应
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
