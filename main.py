from fastapi import Request, FastAPI
import os
from  userDataInterface import  MotherClass, dataInterface, userInterface








app = FastAPI()



@app.get("/")
async def root():
  return {"message": "Hello World"}



@app.post("/signIn")
async def signIn(request: Request):
  data = await request.json()
  userInterface.saveNewUser(data)
  return {"message":  "user saved"} 


@app.post("/logIn")
async def logIn(request: Request):
  data = await request.json()
  userInterface.checkUser(data)
  return {"message": "saved"} 




@app.post("/saveIMG")
async def saveIMG(request: Request):
  data = await request.json()
  dataInterface.ipfs_save_meta( userId = data[MotherClass.key_email], newImg = data[MotherClass.key_img] )
  return {"message": "saved"} 




@app.post("/getData")
async def logIn(request: Request):
  data = await request.json()
  
  resData = await dataInterface.get_OnOffchain_all_ipfsHash(userId= data[MotherClass.key_email], onchain = data[MotherClass.key_onChain], withImg=True)

  return {"message": resData  } 






