from fastapi import APIRouter

router = APIRouter()


@router.get("/items/", response_model=schemas.City)
async def read_city(name: str):
    # todo retrieve city with its data
    return [
        {"id": 1, "name": "Minsk", "country": "Belarus"},
        {"id": 2, "name": "Pinsk", "country": "Belarus"},
        {"id": 3, "name": "Riga", "country": "Latvia"},
        {"id": 4, "name": "Figa", "country": "Karman"},
    ]
