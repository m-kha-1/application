from fastapi import FastAPI,Response,HTTPException

import model

from database import engine



model.Base.metadata.create_all(bind=engine)

APP=FastAPI()


@APP.get("/")
async def get():
    pass

@APP.post("/posts/{post_id}/")
async def create(post_id):
    pass

@APP.put("/posts/{post_id}/")
async def update(post_id):
    pass

@APP.delete("/posts/{post_id}/")
async def delete(post_id):
    pass