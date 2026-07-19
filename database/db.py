# Centralized PostgreSQL database utility for FinTwin AI.

from contextlib import contextmanager
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import Error
from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)

@contextmanager
def get_connection():
    """
    Creates a PostgreSQL connection.

    Usage:
        with get_connection() as conn:
            ...
    """
    connection = None
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            cursor_factory=RealDictCursor
        )

        yield connection

    except Error as e:
        raise RuntimeError(f"Database connection failed: {e}")

    finally:
        if connection is not None:
            connection.close()


def execute_query(query: str, params=None):
    """
    Executes INSERT, UPDATE, DELETE.

    Returns:
        True if successful.
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()

    return True


def fetch_one(query: str, params=None):
    """
    Executes SELECT query and returns one row.
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()


def fetch_all(query: str, params=None):
    """
    Executes SELECT query and returns all rows.
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()


def test_connection():
    """
    Tests database connectivity.
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT version();")
                version = cursor.fetchone()

        print("\n✅ PostgreSQL Connected Successfully!\n")
        print(version)

    except Exception as e:
        print("\n❌ Connection Failed\n")
        print(e)

if __name__ == "__main__":
    test_connection()