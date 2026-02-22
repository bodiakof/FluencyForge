from datetime import date

from api.db import get_connection


class CardRepository:

    def get_new_cards(self, limit: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT TOP (?) *
            FROM cards
            WHERE repetition_count = 0
            ORDER BY card_id
        """, limit)

        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]

        conn.close()
        return results

    def get_due_cards(self, limit: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT TOP (?) *
            FROM cards
            WHERE repetition_count > 0
              AND next_review_date <= CAST(GETDATE() AS DATE)
            ORDER BY next_review_date
        """, limit)

        rows = cursor.fetchall()
        
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]

        conn.close()
        return results

    def get_total_cards(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM cards")
        total = cursor.fetchone()[0]

        conn.close()
        return total
