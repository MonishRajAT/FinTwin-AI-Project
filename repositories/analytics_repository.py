# analytics_repo.py

from database.db import fetch_all

def get_transactions(user_id: int):

    query = """
    SELECT *

    FROM transactions

    WHERE user_id=%s

    ORDER BY transaction_date;
    """

    return fetch_all(
        query,
        (user_id,),
    )