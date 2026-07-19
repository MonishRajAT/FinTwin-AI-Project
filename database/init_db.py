# Initializes the FinTwiin AI PostgreSQL database.
# Creates all required tables if they do not exist.

from database.db import execute_query
from database.schema import ALL_TABLES


def initialize_database():
    print("\nCreating database tables...\n")

    for table in ALL_TABLES:
        execute_query(table)

    print("All tables created successfully.")


if __name__ == "__main__":
    initialize_database()