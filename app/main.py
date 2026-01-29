import logging
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    logging.info("Health check called")
    return {"status": "healthy"}