import sqlite3

conn = sqlite3.connect(
    "sentiment.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sentiment_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    sentiment TEXT,
    confidence REAL
)
""")

conn.commit()

def save_result(text, sentiment, confidence):

    cursor.execute(
        """
        INSERT INTO sentiment_history
        (text, sentiment, confidence)
        VALUES (?, ?, ?)
        """,
        (text, sentiment, confidence)
    )

    conn.commit()

def fetch_results():

    cursor.execute(
        "SELECT * FROM sentiment_history"
    )

    return cursor.fetchall()