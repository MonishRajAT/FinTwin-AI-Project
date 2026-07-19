# Repository responsible for all user-related database operations.
# This layer should ONLY interact wiht the database

from database.db import execute_query, fetch_one

def create_user(full_name: str, email: str, password_hash: str):
    """
    Creates a new user.

    Returns:
        True
    """
    query = """
    INSERT INTO users (
        full_name,
        email,
        password_hash
    )
    VALUES (%s, %s, %s);
    """
    execute_query(
        query,
        (
            full_name,
            email,
            password_hash
        )
    )
    return True

def get_user_by_email(email: str):
    """
    Fetch a user using email.

    Returns:
        dict | None
    """
    query = """
    SELECT *
    FROM users
    WHERE email = %s;
    """
    return fetch_one(query, (email,))

def get_user_by_id(user_id: int):
    """
    Fetch a user using user_id.

    Returns:
        dict | None
    """
    query = """
    SELECT *
    FROM users
    WHERE user_id = %s;
    """
    return fetch_one(query, (user_id,))

def update_password(
    user_id: int,
    password_hash: str
):
    """
    Updates a user's password.
    """
    query = """
    UPDATE users
    SET password_hash = %s
    WHERE user_id = %s;
    """
    execute_query(
        query,
        (
            password_hash,
            user_id
        )
    )
    return True

def delete_user(user_id: int):
    """
    Deletes a user.

    Related records are automatically deleted
    because of ON DELETE CASCADE.
    """
    query = """
    DELETE FROM users
    WHERE user_id = %s;
    """
    execute_query(
        query,
        (user_id,)
    )
    return True