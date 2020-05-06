# Python Application created by G00273895 John Dunne 

import MySQLConnect   #import the file containing connection to MySQL db and MySQL functions to be called in this application
import MongoConnect # import the Mongo file containing connection to mongoDB and functions to be called

def main(): #main function
    display_menu()   # display_menu function will display the menu to the user

    while True: #while statement as per lecture examples
        choice = input("Choice: ")   # User to input menu choice 
        
        #Option 1 to view people in the person table in groups of 2
        if (choice == "1"):
            people = MySQLConnect.view_people() #view_people function called
            display_menu()  #display menu after execution

        #Option 2 show countries by Independence year 
        elif (choice == "2"):
            print("")
            print("Countries by Independence Year")
            print("-------------------------------")
            indp_year = input("Enter Year: ")   #Year input by user stored in variable to be passed to function
            years = MySQLConnect.get_independence(indp_year)  #Calling function from Connect file 
            for year in years:                   #Results stored in variable & for loop used to print out line by line 
                print(year["Name"], "|", year["Continent"], "|", year["IndepYear"]) #print out as per lecture examples
            display_menu()   
        
        #Option 3 add new person to person table
        elif (choice == "3"):
            print("")
            print("Add New Person")
            print("---------------")
            name = input("Name : ") #user input for new person to be added to db
            age = input("Age : ") #will be passed as parameters to the function
            MySQLConnect.add_person(name, age)
            display_menu()

        #Option 4 View countries by name or part thereof
        elif (choice == "4"):
            print("")
            print("Countries by Name")
            print("------------------")
            Country_name = input("Enter Country Name: ")   #User input country name 
            countries = MySQLConnect.get_country_name(Country_name)
            for country in countries:     #loop through each row and print results in requested format
                print(country["Name"], "|", country["Continent"], "|", country["Population"], "|", country["HeadOfState"])
            display_menu()

        #Option 5 View countries by Population < > or =
        elif (choice == "5"):
            print("")
            print("Countries by Pop")
            print("------------------")
            sign = input("Enter < > or =:")  #user input sign, keep asking until valid sign entered
            while sign not in ("<", ">", "="):   # while none of these 3 signs are entered loop will continue to run & ask for valid input
                sign = input("Enter < > or =:")
                if sign in ("<", ">", "="):   # when valid input is entered loop break and move on to take next input
                    break
            pop = int(input("Enter population:")) #user input population as integer
            populations = MySQLConnect.get_country_population()    #function to retrieve all data from country table
            for population in populations:          #loop through all rows of table and check below
                if sign == "<":                     #return countries with pop less than user input
                    if int(population["Population"]) < int(pop):   #Convert to integers, error was met without int(input)
                        print(population["Code"],"|", population["Name"], "|", population["Continent"], "|", population["Population"])
                elif sign == "=":                   #return countries with pop equal to user input
                    if int(population["Population"]) == int(pop):
                            print(population["Code"],"|", population["Name"], "|", population["Continent"], "|", population["Population"])
                elif sign == ">":                   #return countries with pop greater than user input 
                    if int(population["Population"]) > int(pop):
                            print(population["Code"],"|", population["Name"], "|", population["Continent"], "|", population["Population"])
            display_menu()

        #Option 6 MongoDB Find students by address
        elif (choice == "6"):
            print("")
            print("Find Students by Addresses")
            print("------------------")
            Address = input("Enter Address: ") #user input address will be used an input to function
            people = MongoConnect.find(Address)    #call the find function from MongoConnect file
            for p in people: #loop to print results as per lecture example
                print(p["_id"], "|", p["details"] ["name"], "|",  p["details"] ["age"], "|", p["qualifications"])
            display_menu()

        #Option 7 MongoDB Add new course
        elif (choice == "7"): 
            print("")
            print("Add New Course")
            print("------------------")
            ID = input("_id: ")   #User input which will be passed to insert function
            Name = input("Name: ")
            Level = input("Level: ")
            MongoConnect.insert(ID, Name, Level)   #call function insert from MongoConnect file
            display_menu()
        
        # exit application if user clicks x in main menu
        elif (choice == "x"):
            break;         # exit application if user enters x

        else:
            display_menu()  # any keys entered in main menu except above menu will be displayed again

def display_menu():   #Application menu designed as in project spec using examples from lecture demo's as guide
    print("World DB")
    print("---------")
    print("")
    print("MENU")
    print("====")
    print("1 - View People")
    print("2 - View Countries by Independence Year")
    print("3 - Add New Person")
    print("4 - View Countries by name")
    print("5 - View Countries by population")
    print("6 - Find Students by Address")
    print("7 - Add New Course")
    print("x - Exit Application")


if __name__ == "__main__":
    main()    