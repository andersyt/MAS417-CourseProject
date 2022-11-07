import random
import requests
import urllib.request


class apiRequest:
    image_request_endpoint = str
    request_status = True
    json_response = dict
    image_link = str

    # Constructor
    def __init__(self):
        self.api_endpoint = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'
        self.objectId = createRandomObjectId()
        self.image_request_endpoint = str(self.api_endpoint) + str(self.objectId)

    # Sends request to API, sets request status to True or False based on response
    def setRequestStatus(self, image_request_endpoint):
        api_request = requests.get(image_request_endpoint)

        # Converts response to json syntax
        self.json_response = api_request.json()

        # Checks if response contains image link
        if self.json_response.get('primaryImageSmall') is not None:
            self.image_link = self.json_response.get('primaryImageSmall')

            # Checks if imagelink is empty
            if self.image_link == "":
                return False
            print("----------------API RESPONSE----------------\n" \
                  "Art object and image exists with the following parameters:\n" \
                  + "ObjectId: " + str(self.objectId) + ", Title: " + self.json_response.get('title') \
                  + "\nImagelink: " + self.image_link \
                  + "\nImage saved locally under 'resources' folder with the name: art-picture.jpg")

            # Saves the image locally
            urllib.request.urlretrieve(self.image_link, "./resources/art-picture.jpg")

            return True
        else:
            return False

        # Returns a random integer between 1 and 5000


def createRandomObjectId():
    random_objectId = str(random.randint(1, 5000))
    return random_objectId


def main():
    requestObject = apiRequest()


if __name__ == "__main__":
    main()