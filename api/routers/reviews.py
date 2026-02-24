from fastapi import APIRouter, HTTPException

from api.repositories.review_repository import ReviewRepository


router = APIRouter()
repo = ReviewRepository()


@router.post("/review/{card_id}")
def review_card(card_id: int, grade: int):
    if grade not in [1, 2, 3]:
        raise HTTPException(status_code=400, detail="Grade must be 1, 2, or 3")

    try:
        result = repo.review_card(card_id, grade)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    