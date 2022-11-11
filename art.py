import random
import requests
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image
from stl import mesh
import numpy as np

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

    def showImage(self):
        image=Image.open("./resources/art-picture.jpg")
        
        #Get image properties (width and height)
        org_image_width, org_image_height = image.size

        #Checks if image is bigger than 500x500, resizes with thumbnail function and keeps aspect ratio
        if org_image_height > 500 or org_image_width > 500:
            image.thumbnail((500,500), Image.Resampling.LANCZOS)
        
        #Shows image in GUI     
        plt.imshow(image)
        plt.show()

    #Converts image to stl, NOT WORKING BECAUSE OF PACKAGE    
    def convertImageToSTL(self):
        grey_img = Image.open("./resources/art-picture.jpg").convert('L') #Reads image and converts to grey image
        
        max_size =(200,200) #Sets maximum size to fit ultimaker
        max_height=30
        
        grey_img.thumbnail(max_size) 
        imageNp = np.array(grey_img)
        maxPix=imageNp.max()

        (W,H)=grey_img.size

        vertices=[]
        faces=[]

        for Y in range(0, H, 1):
            for X in range(0,W,1):
                pixelIntensity = imageNp[Y][X]
                Z = (pixelIntensity * max_height) / maxPix
                vertices.append((X,Y,Z))
                
        for X in range(0, W-1, 1):
            for Y in range(0, H-1, 1):
                face_v1= X+Y*W
                face_v2=X + 1 + Y* W
                face_v3=X + 1 + (Y+1) * W
                
                faces.append((face_v1,face_v2,face_v3))
                
                face_v1= X+Y*W
                face_v2=X  + (Y+1)* W
                face_v3=X + 1 + (Y+1) * W
                
                faces.append((face_v1,face_v2,face_v3))

        facess_arr = np.array(faces)
        vertices_arr = np.array(vertices)

        image_mesh = mesh.Mesh(np.zeros(facess_arr.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(facess_arr):
            for j in range(3):
                image_mesh.vectors[i][j] = vertices_arr[f[j],:]

        image_mesh.save('./resources/art-picture.stl')
        print("----------------STL CREATION-----------------\nSTL file created under 'resources' folder with the name: art-picture.stl")

# Returns a random integer between 1 and 5000
def createRandomObjectId():
    random_objectId = str(random.randint(1, 5000))
    return random_objectId


def main():
    requestObject = apiRequest()


if __name__ == "__main__":
    main()