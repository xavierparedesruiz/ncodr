from fastapi import FastAPI

from server.routes.qr import router as QRRouter

app = FastAPI()

app.include_router(QRRouter, tags=['QR'], prefix='/qr')


@app.get('/', tags=['Root'])
async def read_root():
    return {'message': 'Welcome to this fantastic app!'}

