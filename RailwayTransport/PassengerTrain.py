from operator import attrgetter
from src.RailwayTransport.Train import Train

class PassengerTrain(Train):

    """Base class for Passengers Train object"""
    def __init__(self,kupeWagons, platskartWagons,luksWagons):
        Train.__init__(self,type,name="N/A",route="N/A")
        self._kupeWagons = kupeWagons
        self._platskartWagons = platskartWagons
        self._luksWagons = luksWagons

    #returns info about list of objects
    def __repr__(self):
        return repr((self._kupeWagons, self._platskartWagons, self._luksWagons))




