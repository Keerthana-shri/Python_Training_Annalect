from fastapi import FastAPI
from logic import Start
app= FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/newfun")
async def newfun():
    c= Start()
    return c.rs()

@app.get("/newfun/")
async def ws(n):
    d= Start()
    e= d.nextnumber(int(n))
    return{"result": e}