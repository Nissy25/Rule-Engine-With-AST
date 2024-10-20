from fastapi import FastAPI
from app.api.routes import router  # Ensure this import is correct

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
