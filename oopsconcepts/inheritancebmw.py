from bmwseries import *


# Duck Typing concept from Polymorphism
def callSeries(obj):
    obj.start()  # functionality of parent class invoked
    print(obj.make)
    print(obj.model)
    print(obj.year)
    obj.stop()  # functionality of parent class invoked
    # obj.display()  # functionality of childclass itself


threeseries = ThreeSeries(True, "BMW", "234i", 2018)
callSeries(threeseries)
print(threeseries.cruisecontrolenabled)

fiveseries = FiveSeries(True, "BMW", "332s", 2019)
callSeries(fiveseries)
print(fiveseries.parkingassistenabled)

"""print(fiveseries.parkingassistenabled)
print(fiveseries.make)
print(fiveseries.model)
print(fiveseries.year)
"""