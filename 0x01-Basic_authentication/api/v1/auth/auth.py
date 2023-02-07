#!/usr/bin/env python3
""" 3. Auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth method
        """
        if path is None or not excluded_paths:
            return True
        path = path + '/' if path[-1] != '/' else path
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ curent_user method
        """
        return None
