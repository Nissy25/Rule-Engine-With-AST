from fastapi import FastAPI
from app.api.routes import router  # Ensure this path is correct

app = FastAPI()

# Include the API routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

