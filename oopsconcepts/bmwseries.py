from bmw import BMW

class ThreeSeries(BMW):

    # contructor of child class
    def __init__(self, cruisecontrolenabled, make, model, year):
        # invoking the contructor of the parent class
        # BMW.__init__(self, make, model, year)

        # using super() to invoke the parent class's contructor
        # and other functionalities
        super().__init__(make, model, year)
        self.cruisecontrolenabled = cruisecontrolenabled

    def display(self):
        print(self.cruisecontrolenabled)

    # overriding/shadowing the fucntionality of parent class
    # Overriding : Implementing the method with the same name
    def start(self):
        # but with the different functionality
        print("Press button to start")

        # but to invoke the parent class's method as well
        # built-in super() is useful
        super().start()


class FiveSeries(BMW):

    def __init__(self, parkingassistenabled, make, model, year):
        # BMW.__init__(self, make, model, year)

        # using super() to invoke the parent class's contructor
        # and other functionalities
        super().__init__(make, model, year)
        self.parkingassistenabled = parkingassistenabled

