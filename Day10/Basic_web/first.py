from fastapi import FastAPI

app= FastAPI()

@app.get("/hi")
async def root():
    return {"message": "Hi World"}