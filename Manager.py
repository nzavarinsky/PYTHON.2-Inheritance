from operator import attrgetter
from src.RailwayTransport.Train import Train
from src.RailwayTransport.PassengerTrain import PassengerTrain
from src.RailwayTransport.PassengersInTrain import PassengersInTrain
from src.RailwayTransport.SearchWagons import SearchWagonsByNumOfPass
from src.RailwayTransport.FreightTrain import FreightTrain
from src.RailwayTransport.Locomotive import Locomotive


class Manager:
    def createLocomotive(self):
        locomotive = Locomotive("Diesel")
        locomotive.toString()

    def createFreightTrain(self):
        freight_train = FreightTrain("Diamonds", 1000)
        freight_train.toString()

    def createPassengerTrain(self):
        train = Train("Passengers",10,"Kobzar","Lviv-Kyiv") #create train object
        search_wag = SearchWagonsByNumOfPass() #calling function for searching
        passengers_in_train = PassengersInTrain(2, 3, 4) #object for passengers in train class

        #creating list of trains for sorting
        trains = [PassengerTrain(kupeWagons=5, platskartWagons=4, luksWagons=3),
                  PassengerTrain(kupeWagons=1, platskartWagons=2, luksWagons=7),
                  PassengerTrain(kupeWagons=100, platskartWagons=50, luksWagons=70)]

        print("Info about passenger train:")
        print(" Name : ", train.get_name(), "\n"
              " Type : ", train.get_type(), "\n"
              " Num of wagons : ", train.get_numOfWagons(), "\n"
              " Route : ", train.get_route(),"")
        print(" Sum of passengers is :", passengers_in_train.sum())
        print("_____________________________\n"
          "Info about train system : ")
        print(" Num of trains :", trains.__len__())
        print("_____________________________\n"
          " Unsorted trains list:")
        print(*trains, sep="\n")
        trains.sort(key=attrgetter('_kupeWagons'))
        print (" Sorted trains list:")
        print(*trains, sep="\n")
        print("______________________________\n"
          " Search wagons by num of passenger")
        search_wag.findWagonsByValue()