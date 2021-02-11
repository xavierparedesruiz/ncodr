from bson.objectid import ObjectId
import motor.motor_asyncio

from server.models.qr import QR

MONGO_DETAILS = "mongodb://root:example@mongo:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.ncodr

qr_collection = database.get_collection('qrs_collection')


def qr_serializer(qr) -> dict:
    qr_id = qr.pop('_id')
    return {'id': str(qr_id), **qr}


async def add_qr(qr_data: QR) -> dict:
    qr = await qr_collection.insert_one(qr_data)
    new_qr = await qr_collection.find_one({"_id": qr.inserted_id})
    return qr_serializer(new_qr)


# Retrieve a QR with a matching ID
async def retrieve_qr(qr_id: str) -> dict:
    qr = await qr_collection.find_one({"_id": ObjectId(qr_id)})
    if qr:
        return qr_serializer(qr)

    return {}
