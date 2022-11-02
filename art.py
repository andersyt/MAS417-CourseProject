import random


#Returns a random integer between 1 and 5000            
def createRandomObjectId():
    random_objectId = str(random.randint(1,5000)) 
    return random_objectId

def main():
    print(createRandomObjectId())

if __name__ == "__main__":
    main()