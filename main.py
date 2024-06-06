from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()

@app.post("/predict")
async def predict(word):
    words = ["hate", "violence", "curse"]
    message = "good" if word.lower() not in words else "bad"
    return {"word": word, "message": message}

if __name__ == "__main__":
    uvicorn.run(app)