import pymongo

myclient = None

#function to connect to mongo daemon
def connect():  
    #print("In Connect()")  #print to see we get into the function ok
    global myclient   #global variable myclient created at beginning of script
    myclient = pymongo.MongoClient()
    myclient.admin.command('ismaster')
    #print(myclient)  #print out on command line connection details

#function for menu option 6
def find(Address):
    if (not myclient): #check are we already connected
        connect() #if not connected connect() function is called
    mydb = myclient["proj20DB"]  #db name
    docs = mydb["docs"]   #collection name 
    #write mongo query here:
    query = [{"$match":{"details.address":{"$eq": Address}}}, {"$project": {"details.name":1, "details.age":1, "qualifications":{"$ifNull":["$qualifications", " "]}}}]
    people = docs.aggregate(query)   #mongo query executed
    return people  #results returned

#function for menu option 7
def insert(ID, Name, Level):
    if (not myclient): #check are we already connected
             connect() #if not connect
    mydb = myclient["proj20DB"]  #db name
    docs = mydb["docs"]   #collection name 
    newDoc = {"_id" : ID, "name" : Name, "level" : Level} #have to put quotes around field names so Python doesnt store them as variables 
    try:
        docs.insert_one(newDoc) #if correct data entered, will be inserted to docs collection
    except pymongo.errors.DuplicateKeyError as e: #added this exception after testing 
        print("*** ERROR ***: _id DATA already exists") #error when existing _id entered 
    except Exception as e: #all other errors
        print("Error:", e)

def main():
    if (not myclient): #check are we already connected
        try:
            connect() #if not connected connect() function is called
        except Exception as e:
            print("Problem connecting to database", e) #any error connecting to db will be printed

#main function called
if __name__ == "__main__":
    main()    