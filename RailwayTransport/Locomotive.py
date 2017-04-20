from src.RailwayTransport.Train import Train

class Locomotive:
    """Basic class for locomotive"""
    def __init__(self,typeOfEngine):
        Train.__init__(self,"Locomotive","N/A","TTE16","Kyiv-Lviv")
        self.typeOfEngine = typeOfEngine

    def get_type_of_engine(self):
        return self.typeOfEngine

    #shows info about this train
    def toString(self):
        print("___________________________\n"
              "Info about locomotive :\n",
              "Name :", Train.get_name(self),"\n",
              "Route :", Train.get_route(self),"\n",
              "Type :", Train.get_type(self), "\n")
