from fastapi import APIRouter

from api.services.card_service import CardService
from api.schemas import CardResponse, TotalCardsResponse


router = APIRouter()
service = CardService()

@router.get("/cards/new", response_model=list[CardResponse])
def get_new_cards(limit: int = 10):
    rows = service.get_new(limit)
    return rows

@router.get("/cards/due", response_model=list[CardResponse])
def get_due_cards(limit: int = 10):
    rows = service.get_due(limit)
    return rows

@router.get("/cards/total", response_model=TotalCardsResponse)
def get_total_cards():
    total = service.get_total()
    return {"total_cards": total}
