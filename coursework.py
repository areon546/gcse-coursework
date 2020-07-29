import csv

"""makes the file into a 2d list with stopping points at ','/ commas"""
def loadAir():
    """makes the file into a 2d list"""

    airports = []

    with open('Airports.txt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')

        for row in spamreader:
            # print(', '.join(row)) #prints row from file
            airports.append(row)
    return airports

"""ends the program, though specifically it just informs the user of the end of the program"""
def quit():  # option e
    """ends the program"""
    print("The program has ended. ")  # closes the program
    pass


"""lets the user decide what airports to go to 
and tell them how far it is from starting airport to destination airport"""
def flightPlan(airports):  # option a
    """asks for airport codes imports and authenticates them"""

    global startingAir
    global destAir

    destAir = ""

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
        return

    """asks for the destinations airport and authenticates it"""
    destAir = input("What airport are you going to? Choose one from the list: " f"{airDestCodes}. ")
    destAir = destAir.upper()

    if destAir in airDestCodes:  # authenticates airport code

        pass
    else:  # error message if wrong airport code
        destAir = ""
        print("ERROR//WRONG DESTINATION CODE")
        return

    """prints full name of airport and distance based on starting airport"""
    for n in airports:  # searches through the 2d list for the appropriate airport through iteration

        if n[0] == destAir:
            print("Airport name ", n[1])  # prints the appropriate airport's name

            """decides on distance from starting airport and destination airport"""
            if startingAir == "LPL":
                print("Distance from Liverpool ", n[2])

            if startingAir == "BOH":
                print("Distance from Bournemouth ", n[3])

            break

"""lts the user decide what type of plane to fly in, and the number of first class that airplane will have"""
def flightDetails():  # option b
    global pType
    global numOfFirstClass

    pType = ""
    numOfFirstClass = 0

    pass


"""calculates the prices and the profit of a flight, amongst other calculations"""
def pricePlanAndProfit():  # option c
    sPrice = 0  # £
    fClassPrice = 0  # £
    pass


"""makes all global variables nada, replacing with a method of returning file later on in production in premise"""
def clear():  # option d
    sPrice = 0  # £
    fClassPrice = 0  # £
    pType = ""
    numOfFirstClass = 0
    startingAir = ""
    destAir = ""
    return


"""the first version of the menu, replaced"""
def menu():
    print("""What do you want to choose? 
    a. Airport details
    b. Flight details
    c. Price plan & profit calculation
    d. Clear data
    e. Quit
    """)

    inp = str(input("So where do you want to go? "))

    while inp != "e":  # makes it so that this runs as long as the user doesnt press "e"
        if inp == "a":  # airport details, plans the starting and destination airports
            flightPlan()

        elif inp == "b":  # flight details, what plane used
            flightDetails()

        elif inp == "c":  # price plan and profit, calculates costs and income, and so profit
            pricePlanAndProfit()

        elif inp == "d":  # clears data
            clear()

        elif inp != "a" or "b" or "c" or "d":
            print("error")
            return



    else:
        quit()


"""second version of the menu, returns back to the menu after use"""
def menu_patryk():
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

        inp = str(input("So where do you want to go? "))  #input string for menu

        if inp == "a":  # airport details, plans the starting and destination airports
            """funtion for menu item 'a'"""
            flightPlan(airports)

        elif inp == "b":  # flight details, what plane used
            """funtion for menu item 'b'"""
            flightDetails()

        elif inp == "c":  # price plan and profit, calculates costs and income, and so profit
            """funtion for menu item 'c'"""
            pricePlanAndProfit()

        elif inp == "d":  # clears data
            """funtion for menu item 'd'"""
            clear()

        elif inp == "e":
            """funtion for menu item 'e'"""
            quit() # starts the 'quit()' funtion
            return 0  # changes it so that the while loop ends by changing the Bool

        else:
            """prints 'ERROR' is the user does something they aren't supposed to"""
            print("ERROR")


menu_patryk()
