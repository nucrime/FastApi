from fastapi import APIRouter

router = APIRouter()

@router.get("/text/", response_model=bool)
def is_sarcastic():
    # todo add lib for semantic analysis and return true or false depending on the result of text analysis on sarcasm
    return True
