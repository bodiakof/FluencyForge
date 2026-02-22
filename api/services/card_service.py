from api.repositories.card_repository import CardRepository


class CardService:

    def __init__(self):
        self.repo = CardRepository()

    def get_new(self, limit: int):
        return self.repo.get_new_cards(limit)

    def get_due(self, limit: int):
        return self.repo.get_due_cards(limit)

    def get_total(self):
        return self.repo.get_total_cards()
