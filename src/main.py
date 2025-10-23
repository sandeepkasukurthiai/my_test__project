from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FASTAPI application!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}    
@app.get("/status")
async def status_check():
    return {"status": "running"}    
