from fastapi import FastAPI

import models, database
from router import user_router

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Include routers
app.include_router(user_router.router)

@app.get("/")
def home():
    return {"message": "PostgreSQL FastAPI CRUD with Age field connected successfully"}
