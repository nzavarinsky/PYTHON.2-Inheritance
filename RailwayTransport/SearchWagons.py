class SearchWagonsByNumOfPass:
    """Basic class for searching wagons by number of passengers"""
    MAX_INPUT_VALUE = 54
    AVERAGE_INPUT_VALUE = 36
    MIN_INPUT_VALUE = 0
    def findWagonsByValue(self):
        inputValue = int(input(" Enter value for search :"))
        if inputValue >= SearchWagonsByNumOfPass.MAX_INPUT_VALUE:
            print(" There are no wagons that can contain this values of passengers")
        if inputValue >= SearchWagonsByNumOfPass.MAX_INPUT_VALUE\
           and inputValue < SearchWagonsByNumOfPass.AVERAGE_INPUT_VALUE:
            print(" Platskart type of wagon")
        if inputValue >= SearchWagonsByNumOfPass.MIN_INPUT_VALUE\
                and inputValue <= SearchWagonsByNumOfPass.AVERAGE_INPUT_VALUE:
            print(" Kupe type of wagons")
