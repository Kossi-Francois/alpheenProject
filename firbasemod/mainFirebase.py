



import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db  as realtime_db

import datetime

import os

cred_path = "/openclasseromConf.json"
cred = credentials.Certificate(os.path.dirname(__file__) + cred_path)
firebase_admin.initialize_app(cred)




class userModel :

    def __init__(self, colName = "collecxxx",) -> None:
        self.db = firestore.client()
        self.colName = colName
        self.col_ref = self.db.collection(self.colName)

        self.methode = {"getAll": self.getAllUser,   "add": self.addUser, "update":self.updateUser}


    def getAllUser(self, *args):
        docs = self.col_ref.stream()
        docs = [ elt.to_dict() for elt in docs]

        return docs


    def addUser(self, users):
        #self.col_ref.document(self.dbName).set(aUser, merge=True)

        for aUser in users:
            aUser["creation_timestamp"] = datetime.datetime.now(tz=datetime.timezone.utc)
            self.col_ref.add(aUser)

        return True


    def updateUser(self, data):

        userID, data2Updtae = data["id"], data["data"]

        batch = self.db.batch()

        for idx, auserID in enumerate(userID):
            user_ref = self.col_ref.document(auserID)
            adata2Updtae = data2Updtae[idx]
            adata2Updtae["lastUpdate_timestamp"] = datetime.datetime.now(tz=datetime.timezone.utc)
            #user_ref.update(adata2Updtae)
            batch.update(user_ref,  adata2Updtae)

        batch.commit()

        return True





myUser  = userModel( colName = "poeProject")

######

class RTDB:
    def __init__(self, refName = "poe"):
        self.dbUrl = "https://openclasserom-test.firebaseio.com/"
        self.rtDB_ref = realtime_db.reference('/tempdata', url = self.dbUrl)

        self.methode = {"getAll": self.getData,   "add": self.update, "delete":self.deleteData}

        self.data = ""


    def getData(self, *args):
        temp = self.rtDB_ref.get()

        return temp


    def setData(self, data):

        return True

    def update(self, data):
        self.rtDB_ref.update( {data["id"]: data}  )
        return True


    def deleteData(self, data):
        users_ref = self.rtDB_ref.child(data["id"])
        users_ref.delete()
        return True


rtdb = RTDB()