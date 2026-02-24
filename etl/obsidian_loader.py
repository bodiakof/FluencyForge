import re
import pyodbc


FILE_PATH = r"F:\Shared Folder\The Vault\ENGLISH\Vocabulary\Flashcards\PVs.md"
DECK_ID = 2

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=FluencyForgeDW;"
    "Trusted_Connection=yes;"
)

CARD_PATTERN = re.compile(
    r"\*\*(.*?)\*\*\s*\?\s*(.*?)\s*(?=<!--SR:|$)",
    re.DOTALL
)


def clean_back_text(text: str) -> str:
    # Remove HTML line breaks
    text = re.sub(r"<br\s*/?>", " ", text)

    # Remove markdown italics: _text_ → text
    text = re.sub(r"_([^_]+)_", r"\1", text)
    
    # Remove markdown italics: *text* → text
    text = re.sub(r"\*([^*]+)\*", r"\1", text)

    # Replace multiple newlines with space
    text = re.sub(r"\s*\n\s*", " ", text)

    # Collapse multiple spaces
    text = re.sub(r"\s{2,}", " ", text)

    return text.strip()


def extract_cards(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    matches = CARD_PATTERN.findall(content)

    cards = []
    for front, back in matches:
        clean_back = clean_back_text(back)
        cards.append((front.strip(), clean_back))

    return cards


def insert_cards(cards):
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()

    inserted = 0
    skipped = 0

    for front, back in cards:
        try:
            cursor.execute(
                """
                INSERT INTO cards (deck_id, front_text, back_text)
                VALUES (?, ?, ?)
                """,
                DECK_ID,
                front,
                back
            )
            inserted += 1

        except pyodbc.IntegrityError:
            skipped += 1

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Inserted: {inserted}")
    print(f"Skipped (duplicates): {skipped}")


def main():
    cards = extract_cards(FILE_PATH)
    print(f"Found {len(cards)} cards.")
    insert_cards(cards)


if __name__ == "__main__":
    main()
