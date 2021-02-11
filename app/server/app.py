from fastapi import FastAPI, Body

from server.routes.qr import router as QRRouter
from server.database import add_qr
from server.models.qr import QR

app = FastAPI()

app.include_router(QRRouter, tags=['QR'], prefix='/qr')


@app.get('/', tags=['Root'])
async def read_root():
    return {'message': 'Welcome to this fantastic app!'}

