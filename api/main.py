from fastapi import FastAPI

from api.routers import cards, reviews


app = FastAPI(title="FluencyForge API")

app.include_router(cards.router)
app.include_router(reviews.router)
