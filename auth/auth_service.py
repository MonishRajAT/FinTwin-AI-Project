"""
Business logic for authentication.

Responsibilities:
- Register users
- Authenticate users
- Validate duplicate emails
"""

from repositories.user_repository import (
    create_user,
    get_user_by_email,
)
from auth.password_utils import (
    hash_password,
    verify_password,
)
from repositories.profile_repository import create_profile

class AuthService:
    """Authentication business logic."""

    @staticmethod
    def register_user(
        full_name: str,
        email: str,
        password: str
    ):
        """
        Register a new user.
        """

        full_name = full_name.strip()
        email = email.strip().lower()

        if not full_name:
            raise ValueError("Full name cannot be empty.")

        if not email:
            raise ValueError("Email cannot be empty.")

        if len(password) < 8:
            raise ValueError(
                "Password must contain at least 8 characters."
            )

        existing_user = get_user_by_email(email)

        if existing_user:
            raise ValueError(
                "An account already exists with this email."
            )

        password_hash = hash_password(password)

        create_user(
            full_name=full_name,
            email=email,
            password_hash=password_hash
        )
        user = get_user_by_email(email)
        create_profile(user["user_id"])
        return {
            "success": True,
            "message": "Registration successful."
        }

    @staticmethod
    def login_user(
        email: str,
        password: str
    ):
        """
        Authenticate a user.
        """

        email = email.strip().lower()

        user = get_user_by_email(email)

        if user is None:
            raise ValueError("Invalid email or password.")

        if not verify_password(
            password,
            user["password_hash"]
        ):
            raise ValueError("Invalid email or password.")

        return {
            "success": True,
            "user": {
                "user_id": user["user_id"],
                "full_name": user["full_name"],
                "email": user["email"],
            }
        }