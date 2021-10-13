# Duck typing using dependency injection

class Flight:
    # using duck typing
    # contructor : with obj as parameter
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        # ivoking a method using obj irrespective of class
        self.engine.start()


class AirbusEngine:
    def start(self):
        print("Starting Airbus engine")


class BoingEngine:
    def start(self):
        print("Starting Boing engine")


ae = AirbusEngine()
be = BoingEngine()

# dynamically injecting the obj to a class
fae = Flight(ae)
fae.startEngine()

# dynamically injecting the obj to a class
fbe = Flight(be)
fbe.startEngine()
