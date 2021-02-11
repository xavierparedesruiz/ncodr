from bson.errors import InvalidId
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import add_qr, retrieve_qr
from server.models.qr import QR

router = APIRouter()


@router.post('/', response_description='QR data added into the database')
async def add_qr_data(qr: QR = Body(...)):
    encoded_qr = jsonable_encoder(qr)
    new_qr = await add_qr(encoded_qr)

    return new_qr


@router.get('/{qr_id}', response_description='Retrieve QR data')
async def get_qr_data(qr_id):
    try:
        found_qr = await retrieve_qr(qr_id)
    except InvalidId:
        return {"message": "Invalid ObjectId"}

    return found_qr
