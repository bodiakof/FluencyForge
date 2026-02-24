from datetime import date, timedelta

from api.db import get_connection


class ReviewRepository:

    def review_card(self, card_id: int, grade: int):
        conn = get_connection()
        cursor = conn.cursor()

        # Fetch current card state
        cursor.execute("""
            SELECT repetition_count,
                   current_interval,
                   ease_factor
            FROM cards
            WHERE card_id = ?
        """, card_id)

        row = cursor.fetchone()

        if not row:
            conn.close()
            raise ValueError("Card not found")

        repetition_count, current_interval, ease_factor = row

        previous_interval = current_interval
        previous_ease_factor = ease_factor

        # Calculate new interval
        if repetition_count == 0:
            if grade == 1:      # Hard
                interval = 1
            elif grade == 2:    # Good
                interval = 2
            else:               # Easy
                interval = 4
        else:
            if grade == 1:
                interval = 1
            elif grade == 2:
                interval = round(current_interval * ease_factor)
            else:
                interval = round(current_interval * ease_factor * 1.3)

        # Update ease factor
        if grade == 1:
            ease_factor -= 0.2
        elif grade == 3:
            ease_factor += 0.15

        ease_factor = max(ease_factor, 1.3)

        # Compute next review date
        next_review_date = date.today() + timedelta(days=interval)

        new_repetition_count = repetition_count + 1

        # Insert review event (user_id hardcoded = 1)
        cursor.execute("""
            INSERT INTO review_events (
                user_id,
                card_id,
                review_grade,
                previous_interval,
                new_interval,
                previous_ease_factor,
                new_ease_factor
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            1,
            card_id,
            grade,
            previous_interval,
            interval,
            previous_ease_factor,
            ease_factor
        )

        # Update card state
        cursor.execute("""
            UPDATE cards
            SET repetition_count = ?,
                current_interval = ?,
                ease_factor = ?,
                next_review_date = ?
            WHERE card_id = ?
        """,
            new_repetition_count,
            interval,
            ease_factor,
            next_review_date,
            card_id
        )

        conn.commit()
        conn.close()

        return {
            "card_id": card_id,
            "new_interval": interval,
            "new_ease_factor": ease_factor,
            "next_review_date": next_review_date
        }
    