from typing import Optional

from fastapi import FastAPI, File, UploadFile

from routers import deeplearning_api
app = FastAPI(    
    title="Deeplearning Inference API",
    description="AiBharata Deeplearning Inference API",
    version="v1.0",
    openapi_url="/openapi.json",
    )
app.include_router(deeplearning_api.router, prefix='/api')  

@app.get('/')
async def root():
    return {"Message": "Hello World.. I'm AI.. Bharata!!"}

@app.get('/healthcheck', status_code=200)
async def healthstatus():
    return {"Status": "I am Up.. and Up .. and Up Running"}


import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

