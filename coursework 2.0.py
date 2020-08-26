import csv

def loadAir():
    """makes the file into a 2d list with stopping points at ','/ commas"""

    airports = []

    with open('Airports.txt') as csvFile:
        spamReader = csv.reader(csvFile, delimiter=',') # todo WHY SPAM READER???
        # spamREader is essentially the whiole text, the line creates a 2d list seperated by the line end and the
        # inner lists are seperated by the delimiter

        for row in spamReader:  #
            # print(', '.join(row)) #prints row from file
            airports.append(row)
    return airports

def quitProgram():  # option e
    """ends the program, though specifically it just informs the user of the end of the program"""
    print("The program has ended. ")  # closes the program
    pass

def flightPlan(airports):  # option a
    """lets the user decide what airports to go to
    and tell them how far it is from starting airport to destination airport"""

    """asks for airport codes imports and authenticates them"""

    """makes the airport codes into a list"""
    airDestCodes = []
    for n in airports:
        # print(n[0]) prints airport codes
        airDestCodes.append(n[0])  # makes the codes into a list

    """asks for the starting airport and authenticates it"""
    startingAir = input("What airport are your starting from? Liverpool, LPL; or Bournemouth, BOH ")
    startingAir = startingAir.upper()
    if startingAir == "LPL" or startingAir == "BOH":
        pass
    else:
        startingAir = ""
        print("ERROR//WRONG STARTING CODE")
        return None, None, None

    """asks for the destinations airport and authenticates it"""
    destAir = input("What airport are you going to? Choose one from the list: " f"{airDestCodes}. ")
    destAir = destAir.upper()

    if destAir in airDestCodes:  # authenticates airport code
        pass
    else:  # error message if wrong airport code
        destAir = ""
        print("ERROR//WRONG DESTINATION CODE")
        return None, None, None

    """prints full name of airport and distance based on starting airport"""
    for n in airports:  # searches through the 2d list for the appropriate airport through iteration

        if n[0] == destAir:
            print("Airport name ", n[1])  # prints the appropriate airport's name

            """decides on distance from starting airport and destination airport"""
            if startingAir == "LPL":
                print("Distance from Liverpool ", n[2])
                dist = int(n[2])

            if startingAir == "BOH":
                print("Distance from Bournemouth ", n[3])
                dist = int(n[3])

            break

    return startingAir, destAir, dist

def flightDetails():  # option b
    """lts the user decide what type of plane to fly in, and the number of first class that airplane will have"""

    pType = input("""What plane type do you want to choose: 
        s. small
        m. medium
        l. large
    """)

    pType = pType.lower()
    pTypes = ["s", "m", "l"]
    if pType not in pTypes:
        print("ERROR//WRONG PLANE TYPE")
        return None, None, None, None, None, None

    if pType == "s":  # data for small plane type
        costPSeat = 8
        maxDist = 2650
        maxCap = 180  # without considering #. of first class
        minFirstClass = 8

    if pType == "m":  # data for medium plane type
        costPSeat = 7
        maxDist = 5600
        maxCap = 220  # without considering #. of first class
        minFirstClass = 10

    if pType == "l":  # data for large plane type
        costPSeat = 5
        maxDist = 4050
        maxCap = 406  # without considering #. of first class
        minFirstClass = 14

    # prints data for the planes
    print(f"""Plane details: 
    Cost per seat = {costPSeat}
    Maximum flying distance = {maxDist}
    Maximum human capacity, presuming no first class = {maxCap}
    Minimum first class requirement = {minFirstClass}
""")

    numFirstClass = int(input("How many first class seat do you want? "))
    if numFirstClass >= minFirstClass and numFirstClass < (0.5 * maxCap):  # checks if:
        # number of first class is more than minimum and
        # if number of first class is less than limit
        numStandClass = (maxCap - (2 * numFirstClass))
    else:  # error message if out of bounds
        print(f"ERROR//CANNOT HAVE LESS THAN {minFirstClass}")
        return None, None, None, None, None, None

    return costPSeat, maxDist, maxCap, minFirstClass, numFirstClass, numStandClass

def pricePlanAndProfit(startAir, destAir, dist, costPSeat, maxDist, maxCap,
                       minFirstClass, numFirstClass, numStandClass):  # option c
    """calculates the prices and the profit of a flight, amongst other calculations"""
    

    """checks is some of the earlier processes where finished by checking if there is stuff in the variables"""
    if None in [startAir, destAir, dist,  # checks if any of the variables in this list are empty
                       costPSeat, maxDist, maxCap,
                       minFirstClass, numFirstClass,
                       numStandClass]:
        print("ERROR//FIRST ENTER FLIGHT PLAN AND FLIGHT DETAILS")
        return


    """checks if the plane can fly that far"""
    if dist <= maxDist:
        pass
    else:
        print("ERROR//PLANE TYPE CAN'T REACH THAT FAR")
        return

    sPrice = int(input("What price are the standard seats going to be? "))
    fClassPrice = int(input("What price are the first class seats going to be? "))


    """checks if the plane prices are positive"""
    if sPrice > 0 and fClassPrice > 0:
        pass
    else:
        print("ERROR//FIRST CLASS AND STANDARD CLASS PRICE NEED TO BE MORE THAN ZERO")
        return


    """calculates flight info"""
    numSeats = numStandClass + numFirstClass  # total number of seats
    flightCostPerSeat = costPSeat * (dist/100)  # how expensive flying the a single seat is
    flightCost = flightCostPerSeat * numSeats  # costs for flying that flight
    flightIncome = (sPrice * numStandClass) + (fClassPrice * numFirstClass)  # income for that flight
    flightProfit = flightIncome - flightCost  # profit from the flight

    print(f"""Flight info: 
Number of available seats = {numSeats}
Cost per seat = {flightCostPerSeat}
Flight cost = {flightCost}
Flight revenue = {flightIncome}
Flight profit = {flightProfit}
""")  # prints flight information, by variable

    pass

def menuCycle():
    """second version of the menu, returns back to the menu after use"""

    destAir = None
    startAir = None
    dist = None
    costPSeat = None
    maxDist = None
    maxCap = None
    minFirstClass = None
    numFirstClass = None
    numStandClass = None
    airports = loadAir()

    while 1:  # makes it so that this runs as long as the user doesnt press "e"
        """this loop puts the function at an infinite loop provided that the user doesn't end it"""

        print("""\
        
        Your choices are:  
		    a. Airport details
		    b. Flight details
	    	c. Price plan & profit calculation
	    	d. Clear data
	    	e. Quit
	    	""")

        inp = str(input("So where do you want to go? "))  # input string for menu

        if inp == "a":  # airport details, plans the starting and destination airports
            """funtion for menu item 'a'"""
            startAir, destAir, dist = flightPlan(airports)  # saves info from flightPlan() into variables
            # in form of strings now, due to the fact that there are multiple variables waiting for the
            # outputed info in a certain order

        elif inp == "b":  # flight details, what plane used
            """funtion for menu item 'b'"""
            costPSeat, maxDist, maxCap, minFirstClass, numFirstClass, numStandClass = flightDetails()  # saves info
            # from flightDetails() into variables in form of tuples


        elif inp == "c":  # price plan and profit, calculates costs and income, and so profit
            """funtion for menu item 'c'"""
            pricePlanAndProfit(startAir, destAir, dist,
                       costPSeat, maxDist, maxCap,
                       minFirstClass, numFirstClass,
                       numStandClass)



        elif inp == "d":  # clears data
            """funtion for menu item 'd'"""
            destAir = None
            startAir = None
            dist = None
            costPSeat = None
            maxDist = None
            maxCap = None
            minFirstClass = None
            numFirstClass = None
            numStandClass = None

            print("You've cleared the data. ")

        elif inp == "e":
            """funtion for menu item 'e'"""
            quitProgram()  # starts the 'quit()' funtion
            return 0  # changes it so that the while loop ends by changing the Bool

        else:
            """prints 'ERROR' is the user does something they aren't supposed to"""
            print("ERROR")


menuCycle()
