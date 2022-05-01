


import json
import os
import requests
from pinatapy import PinataPy

import uuid


class IPFS_PINATA:

    key_IpfsHash = "IpfsHash"
    Pinata_API_Key = "Pinata_API_Key"
    Pinata_API_Secret = "Pinata_API_Secret"

    def __init__(self, ):
        # Connect to the IPFS cloud service
        #load_dotenv()  
        credentials = json.load(open(os.path.dirname(__file__) + "/credentials.json","r") )


        pinata_api_key=str(credentials[self.Pinata_API_Key]  )
        pinata_secret_api_key=str(credentials[self.Pinata_API_Secret]  )

        self.pinata = PinataPy(pinata_api_key,pinata_secret_api_key)
        self.gateway="https://ipfs.io/ipfs/"
        #gateway="https://gateway.pinata.cloud/ipfs/"


    def saveFile(self, dataTxt ):
        # Upload the file
        filname =  str(uuid.uuid4()) + ".txt"

        text_file = open(filname, "w")
        text_file.write(dataTxt)

        result = self.pinata.pin_file_to_ipfs(filname)
        # Should return the CID (unique identifier) of the file

        text_file.close()

        print(result)
        return result



    def getFile(self, IpfsHash):
        return requests.get(url= myIPFS.gateway+IpfsHash).text


    def info(self, ):
        # Anything waiting to be done?
        print(pinata.pin_jobs())

        # List of items we have pinned so far
        print(pinata.pin_list())
        
        # Total data in use
        print(pinata.user_pinned_data_total())




myIPFS = IPFS_PINATA()