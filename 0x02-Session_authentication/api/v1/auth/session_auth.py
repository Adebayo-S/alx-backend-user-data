#!/usr/bin/env python3

"""
SessionAuth module
"""

from api.v1.auth.auth import Auth
from typing import TypeVar
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    SessionAuth class.
    """
