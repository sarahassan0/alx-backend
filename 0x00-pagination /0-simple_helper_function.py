#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """ tuple that have the start index and the end index """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
