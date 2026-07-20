# Database operations for transactions.

from database.db import (
    execute_query,
    fetch_one,
    fetch_all,
)

def create_transaction(
        user_id: int,
        transaction_date,
        merchant: str,
        category: str,
        amount: float,
        transaction_type: str,
        payment_method: str,
        currency: str,
        recurring: bool,
        notes: str,
):
    """
    Create a new transaction.
    """

    query = """
    INSERT INTO transactions(

        user_id,
        transaction_date,
        merchant,
        category,
        amount,
        transaction_type,
        payment_method,
        currency,
        recurring,
        notes

    )

    VALUES(

        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s

    );
    """
    execute_query(
        query,
        (
            user_id,
            transaction_date,
            merchant,
            category,
            amount,
            transaction_type,
            payment_method,
            currency,
            recurring,
            notes,
        )
    )

def get_transaction(transaction_id: int):
    query = """
    SELECT *

    FROM transactions

    WHERE transaction_id=%s;
    """

    return fetch_one(
        query,
        (transaction_id,),
    )

def get_transactions(user_id: int):

    query = """
    SELECT *

    FROM transactions

    WHERE user_id=%s

    ORDER BY transaction_date DESC;
    """

    return fetch_all(
        query,
        (user_id,),
    )

def update_transaction(
    transaction_id,
    transaction_date,
    merchant,
    category,
    amount,
    transaction_type,
    payment_method,
    currency,
    recurring,
    notes,
):
    
    query = """
    UPDATE transactions

    SET

    transaction_date=%s,

    merchant=%s,

    category=%s,

    amount=%s,

    transaction_type=%s,

    payment_method=%s,

    currency=%s,

    recurring=%s,

    notes=%s

    WHERE transaction_id=%s;
    """

    execute_query(
        query,
        (
            transaction_date,
            merchant,
            category,
            amount,
            transaction_type,
            payment_method,
            currency,
            recurring,
            notes,
            transaction_id,
        ),
    )

def delete_transaction(transaction_id: int):

    query = """
    DELETE

    FROM transactions

    WHERE transaction_id=%s;
    """

    execute_query(
        query,
        (transaction_id,),
    )
