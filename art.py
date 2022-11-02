import random

class apiRequest:
    image_request_endpoint = str
    request_status = True
    json_response = dict
    image_link = str
    
    #Constructor
    def __init__(self):
        self.api_endpoint = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'
        self.objectId = createRandomObjectId()
        self.image_request_endpoint = str(self.api_endpoint) + str(self.objectId)
        

#Returns a random integer between 1 and 5000            
def createRandomObjectId():
    random_objectId = str(random.randint(1,5000)) 
    return random_objectId

def main():
    requestObject = apiRequest()

if __name__ == "__main__":
    main()