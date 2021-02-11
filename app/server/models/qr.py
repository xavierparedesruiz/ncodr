from enum import Enum

from pydantic import BaseModel, Field


class QRType(str, Enum):
    order = 'order'
    fish = 'fish'
    crate = 'crate'
    unknown = 'unknown'


class QR(BaseModel):
    type: QRType = Field(default=QRType.unknown)
    content: dict = Field(...)

    class Config:
        title = 'QR'
        schema_extra = {
            "example": {
                "id": "uuid",
                "type": "order",
                "content": {
                    "batch": 55643,
                    "reference": 7884434,
                    "staging_area": 'C',
                    "crate_id": 1,
                    "position": 2
                },
            }
        }
