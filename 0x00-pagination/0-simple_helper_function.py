#!/usr/bin/env python3
"""
    0-simple_helper_function.py
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    The function that returns a tuple of size two
    containing start index and the end index.

    """
    first_index = 1 * (page * page_size) - page_size
    last_index = first_index + page_size

    result = (first_index, last_index)
    return result
