from src.RailwayTransport.PassengerTrain import PassengerTrain
class PassengersInTrain:
    """Basic class for searching wagons"""
    def __init__(self,kupeWagons=0,platskartWagons=0,luksWagons=0):
        PassengerTrain.__init__(self,5,4,3)
        self.kupeWagons = kupeWagons
        self.platskartWagons = platskartWagons
        self.luksWagons = luksWagons

    #calculates a sum of passengers in train
    def sum(self):
        kupePassengers = self.kupeWagons * 36
        platskartPassengers = self.platskartWagons * 36
        luksPassengers = self.luksWagons * 36
        return kupePassengers + platskartPassengers + luksPassengers