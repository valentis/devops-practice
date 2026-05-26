# BEFORE (vulnerable)
# query = f"SELECT * FROM items WHERE name LIKE '%{user_input}%'"

# AFTER (safe)
def search_items(db, user_input: str) -> list:
    query = "SELECT * FROM items WHERE name LIKE ?"
    return db.execute(query, (f"%{user_input}%",)).fetchall()
