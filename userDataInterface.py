

from firbasemod.mainFirebase import myUser, rtdb
from ipfsmod.mainIPFS import IPFS_PINATA, myIPFS

import json
import uuid





class MotherClass:

    key_img = "key_img"

    key_email = "email"
    key_mdp   = "mdp"

    key_onChain = "key_onChain"

    key_nft = "key_nft"


    def __init__(self, ):
        return




class User_Data_Interface(MotherClass):

    
    key_ipfs = "key_ipfs"
    
    

    

    def __init__(self, ):

        return


    def get_uniqueDefaultData(self, ):
        return {self.key_onChain : False, self.key_ipfs : {},  self.key_nft: {} }
    


    def getDefaultData(self, userId):

        data = rtdb.getAData(userId)

        if data == None:
            data = {  }

        else: 
            #data = json.loads(data)
            data = data

        return data



    def ipfs_save_meta(self, userId, newImg):
        

        newdata = self.get_uniqueDefaultData()

        newdata[self.key_ipfs  ] = myIPFS.saveFile(newImg)

        data = self.getDefaultData( userId)
        data[ str(uuid.uuid4()) ] = newdata

        rtdb.setData(userId,  data  )
        #app_json = json.dumps(personDict )

        return True



    def get_all_ipfsHash(self, userId, withImg=True, maxData = 10):

        data = self.getDefaultData( userId)

        if withImg:
            for  aKey in list(data.keys())[:maxData]:
                data[aKey][self.key_img] = myIPFS.getFile(data[aKey][self.key_ipfs][ IPFS_PINATA.key_IpfsHash])

        return data



    def get_OnOffchain_all_ipfsHash(self, userId, onchain = False, withImg=True):

        data = self.get_all_ipfsHash( userId, withImg)

        data_onChain = {}
        data_offChain = {}

        for aKey in data.keys():
            if data[aKey][self.key_onChain]:
                data_onChain[aKey] = data[aKey]
            else:
                data_offChain[aKey] = data[aKey]

        return data_onChain if onchain else data_offChain


    def onChain_confirmation(self, userId, dataId):

        data = self.getDefaultData(userId)

        data[dataId][self.key_onChain]  = True

        rtdb.setData(userId,  data )

        return True




dataInterface = User_Data_Interface()







class User_Auth_Interface(MotherClass):



    def __init__(self):
        return 


    def saveNewUser(self, data):

        data["id"] = str(data[self.key_email])
        print( data["id"] )

        myUser.addaUser(data)
        return True


    def checkUser(self, data):
        allUser = myUser.getAllUser()
        currentUser = allUser.get(data[self.key_email] )

        if currentUser ==  None:
            return 0

        else:
            if currentUser[self.key_mdp] == data[self.key_mdp]:
                return 1
            else:
                return 2




userInterface = User_Auth_Interface()