from src.RailwayTransport.Train import Train

class FreightTrain:
    """Basic class for FreightTrain"""
    def __init__(self,typeOfCargo="N/A",weightOfCargo=0):
        Train.__init__(self,"Cargo train",30,"Gruzovichok","Odessa-Kiev")
        self.typeOfCargo = typeOfCargo
        self.weightOfCargo = weightOfCargo

    def get_type_of_cargo(self):
        return self.typeOfCargo

    def get_weight_of_cargo(self):
        return self.weightOfCargo

    #shows info about this train
    def toString(self):
        print("___________________________\n"
              "Info about freight train :\n",
              "Name :", Train.get_name(self),"\n",
              "Num of wagons :", Train.get_numOfWagons(self),"\n",
              "Route :", Train.get_route(self),"\n",
              "Type :", Train.get_type(self), "\n",
              "Type and weight of cargo :", self.typeOfCargo,
              "and", self.weightOfCargo, "kg\n",
              "____________________________")


