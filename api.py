from fastapi import FastAPI

app = FastAPI()

@app.get("/get")
def get_data():
    return {"response": "toto"}
