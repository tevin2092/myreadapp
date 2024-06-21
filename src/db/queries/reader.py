from src.db.database import Database

def insert_data(username: str, title: str, first_name: str, last_name: str):
    conn = Database()

    query = """
        INSERT INTO project.reader(
        username,
        title,
        first_name,
        last_name
        ) VALUES(%s, %s, %s, %s)RETURNING *;
    """

    with conn.cursor() as cursor:
        cursor.ex(query, (username, title,first_name, last_name))
        reader = cursor.fetchone()
        conn.commit()
        return reader