class Train:
    """Base class for train object"""
    def __init__(self,type="N/A",numOfWagons=0,name="N/A",route="N/A"):
        self._type = type
        self._numOfWagons = numOfWagons
        self._name = name
        self._route = route

    def get_type(self):
        return self._type

    def get_name(self):
        return self._name

    def get_numOfWagons(self):
        return self._numOfWagons

    def get_route(self):
        return self._route