# Secure password hashing utilities for FinTwin AI.
# This module is responsible ONLY for hashing and verifying passwords.

import bcrypt

def hash_password(password: str) -> str:
    """
    Hash a plain-text password.

    Args:
        password: User's plain-text password.

    Returns:
        Hashed password as a UTF-8 string.
    """

    if not password:
        raise ValueError("Password cannot be empty.")

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt(rounds=12)
    )

    return hashed_password.decode("utf-8")


def verify_password(
    password: str,
    hashed_password: str
) -> bool:
    """
    Verify a password against its hash.

    Args:
        password: Plain-text password.
        hashed_password: Stored bcrypt hash.

    Returns:
        True if password matches.
        False otherwise.
    """

    if not password or not hashed_password:
        return False

    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


if __name__ == "__main__":

    sample_password = "FinTwin@123"

    hashed = hash_password(sample_password)

    print("Original Password :", sample_password)
    print("Hashed Password   :", hashed)

    print(
        "Password Match    :",
        verify_password(sample_password, hashed)
    )