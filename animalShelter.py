from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
            if username and password:
                print("username and password are:", username, password)
                #Login to mongo 
                self.client = MongoClient('mongodb://%s:%s@localhost:29867/AAC' % (username, password))
                #Assign database
                self.database = self.client['aac']
                print("Connection was successful")
      
    
# Complete this create method to implement the C in CRUD.         
# Define create method
    def create(self, data):
        if data is None:
            print("Error: Insert data was not successful")
            return False
        else:
            #Try to isert and if fails an error will be raised
            try:
                #Checking if data is empty 
                if len(data) == 0:
                    print("Error: Insert data was not successful, create data empty")  
                    return False
                else:
                    #Insert into database 
                    self.database.animals.insert_one(data)
                    print("Insert data successful")
                    return True
            except:
                print("Error: Insert data was not successful")
                return False
                      

# Create method to implement the R in CRUD. 
    def read(self, search):
        if search is None:
            print("Error: Read data was not successful")
            return False
        else:
            try:
                #Checking if search is empty 
                #if len(search) == 0:
                    #print("Error: Read data was not successful. Search term empty")
                    #return False
                #else:
                    #Call to mongo to search database 
                    result = self.database.animals.find(search,{"_id":False})
                    print("Read is successful")
                    return result 
            except:
                print("Error: Read data was not successful")
                return False

                     
# Create method to implement the U in CRUD. 
    def update(self, search, updateData):
        if search is None:
            errorMessage = ("Update failed due to bad search parameters")
            print(errorMessage)
            return False 
        else:
            if updateData is None:
                errorMessage = ("Update failed due to bad update parameters")
                print(errorMessage)
                return False 
            else:
                if len(search) == 0 or len(updateData) == 0:
                    print("Error: Update data was not successful. Search term empty or update data is empty")
                    return False   
                else:
                    try:
                        #Call to mongo so that we can update many 
                        updateResult = self.database.animals.update_many(search, updateData)
                        print("Update was successful")
                        print (updateResult.modified_count, " entries updated")
                        return updateResult
                    except:
                        print("Error: Update was not successful")
                        return False
            
# Create method to implement the D in CRUD.                    
    def delete(self, deleteData):
        if deleteData is None:
            errorMessage = ("Delete failed due to bad delete parameters")
            print(errorMessage)
            return False 
        else:
            if len(deleteData) == 0:
                    print("Error: Delete data was not successful. Delete term empty")
                    return False
            else:      
                try:
                    #Using delete many function to delete from database 
                    deleteResult = self.database.animals.delete_many(deleteData)
                    print("Delete is successful")
                    print (deleteResult.deleted_count, " entries deleted")
                    return deleteResult
                except:
                    print("Error: Delete was not successful")
                    return False
                 
