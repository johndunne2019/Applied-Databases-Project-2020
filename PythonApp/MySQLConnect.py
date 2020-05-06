# The purpose of this file is to connect to the World database in MySQL
# Users please note my should enter your own username and password for connection to MySQL on your local machine
# The functions written in this file are called from the main Python Application file submitted alongside this file

import pymysql  

conn = None   
# function to connect to world database
def connect():    #connect to world db as per lectures 
    global conn   #note other users should enter their own credentials
    conn = pymysql.connect(host="localhost", user="root", password="1992", db="world", cursorclass=pymysql.cursors.DictCursor)

#function for option 1 on the application, completed & working
def view_people():
    if (not conn): # if not connected call the connect function to connect to db
        connect()
    sql = "SELECT * from person"   #everything selected from person table
    with conn: # do the following with connection
        cursor = conn.cursor() #activate cursor
        cursor.execute(sql)   #execute the sql command given above
        while True: #while statement as per lecture examples
            people = cursor.fetchmany(size = 2)    # fetchmany set to size 2 to return 2 rows only & store in people variable 
            # fetchmany documentation: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchmany.html
            for p in people: #loop through each row of data
                print(p["personID"], "|", p["personname"], "|", p["age"]) #print out in correct format as in lecture examples
            quit = input("-- Quit == <q>") # I will ask the user for an input on each iteration of the loop
            if quit == "q": #if the user input is q print below message and break out of loop
                print("Program exited, return to main menu")
                break # loop will break if user inputs q 
        

#function for option 2 on application - completed & working 
def get_independence(indp_year):
    if (not conn):
        connect() 
    sql = "SELECT Name, Continent, IndepYear FROM country WHERE IndepYear = %s"   
    with conn:  #%s is a placeholder for the number that will be passed in as input
        try:
            cursor = conn.cursor() #activate cursor
            cursor.execute(sql, (indp_year))   #user input will be passed to sql command 
            return cursor.fetchall()     #return all the rows that are equal to the user inputted year for independence year
        except pymysql.err.IntegrityError as e:
            print(e)   #Exceptions added as per lecture examples
        except pymysql.err.InternalError as e:
            print(e)


#function for option 3 on application - completed & working 
def add_person(name, age):
    if (not conn):
        connect()
    sql = "INSERT into person (personname, age) VALUES (%s, %s)"    #%s placeholder for user inputs
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (name, age)) #same values as in function above 
            conn.commit()  #commit insertion to database
        except pymysql.err.IntegrityError as e: #Exception added to print out message as per project spec
            print("*** ERROR ***:", name, "already exists")   #Integrity error occurs when user will try to enter name already in db
        except pymysql.err.InternalError as e: #other errors will ba caught here
            print(e)    

# function for option 4 on application - completed & working
def get_country_name(Country_name):
    if (not conn):
        connect()
    sql = """
            SELECT Name, Continent, Population, HeadOfState from country
            where Name like %s       
            """                 #%s is a placeholder for user input
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, ("%"+Country_name+"%")) #concatenate % before & after user input to return any countries with partial matches
            return cursor.fetchall()
        except pymysql.err.IntegrityError as e: 
            print(e)   
        except pymysql.err.InternalError as e: 
            print(e)

#function for option 5 completed & working
def get_country_population():    
    if (not conn):
        connect()
    sql = """
        SELECT * from country    
        """
    with conn:     #retrieve all data from the country table, will print out what matches criteria in application
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except pymysql.err.IntegrityError as e: 
            print(e)   #Exceptions as per examples in lectures
        except pymysql.err.InternalError as e: 
            print(e)

def main():
    if (not conn): #check are we already connected
        try:
            connect() #if not connected connect() function is called
        except Exception as e:
            print("Problem connecting to database", e) #any error connecting to db will be printed

#main function called
if __name__ == "__main__":
    main()   