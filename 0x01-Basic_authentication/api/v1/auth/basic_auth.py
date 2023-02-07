#!/usr/bin/env python3
"""Representation of BasicAuth class
"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract based64 authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return "".join(authorization_header.split()[1:])
