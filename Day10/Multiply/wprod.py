from fastapi import FastAPI
from lprod import Multi

app = FastAPI()

@app.get("/multiply/{a}")
async def root(a: int, b: int):
    if a == 0 or b == 0:
        return {"message": "input was zero"}
    c = Multi()
    d = c.multiply(a, b)
    return {"message": "success", "result": d}