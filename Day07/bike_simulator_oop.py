class Motorcyle:
    def __init__(self  , model):
        self.model = model
        self.is_engine_on = False
    def start_engine(self):
        if self.is_engine_on == False:
            self.is_engine_on = True
            print("Vroom! Engine is now ON")
        else:
            print("Engine is Already ON")
    def turn_off_engine(self):
        if self.is_engine_on == True:
            self.is_engine_on = False
            print("Engine is now OFF")
        else:
            print("Engine is already Off")

my_bike = Motorcyle("Honda CG 125")
my_bike.start_engine()
my_bike.turn_off_engine()
        
        