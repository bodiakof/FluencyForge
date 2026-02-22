from pydantic import BaseModel
from datetime import date

class CardResponse(BaseModel):
    card_id: int
    deck_id: int
    front_text: str
    back_text: str
    repetition_count: int
    current_interval: int
    ease_factor: float
    next_review_date: date | None


class ReviewRequest(BaseModel):
    user_id: int
    review_grade: int
    response_time_ms: int | None = None


class TotalCardsResponse(BaseModel):
    total_cards: int
