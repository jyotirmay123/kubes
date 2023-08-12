from fastapi import FastAPI

app = FastAPI()

@app.get("/add_two/{number}")
async def add_two(number: int):
    result = number + 3
    return {"result": result}


@app.get("/add_three/{number}")
async def add_three(number: int):
    result = number + 3
    return {"result": result}