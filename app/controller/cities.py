from fastapi import APIRouter
from OSMPythonTools.nominatim import Nominatim

router = APIRouter()


@router.get("/maps/")
async def read_maps(name: str):
    # using name retrieve map objects
    nominatim = Nominatim()
    return nominatim.query(name)
