#!/usr/bin/env python3
"""
    0-simple_helper_function.py
"""
from typing import Tuple
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """The function that return content of the page"""
        assert isinstance(page, int) and page > 0, "page must be greatern 0"
        assert isinstance(
            page_size, int) and page_size > 0, "page size must be greatern 0"

        datasetList = self.dataset()
        index = index_range(page, page_size)
        # print(index[0])
        # print(index[1])
        # print(f"len {len(datasetList)}")

        if 0 <= index[1] > len(datasetList) or index[0] > len(datasetList):
            return []
        result = [datasetList[i] for i in range(index[0], index[1])]
        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """"
        returns a dictionary that contain page_size, page, data,
        next_page, prev_page and the total page
        """
        total_pages = 1
        res = {
            'page_size': 0,
            'page': 0,
            'data': [],
            'next_page': None,
            'prev_page': None,
            'total_pages': 0
        }

        res['data'] = self.get_page(page, page_size)
        res['page_size'] = len(self.get_page(page, page_size))
        res['page'] = page
        if len(self.get_page(page + 1, page_size)) != 0:
            res['next_page'] = page + 1

        if page > 1 and len(self.get_page(page - 1, page_size)) != 0:
            res['prev_page'] = page - 1
        else:
            res['prev_page'] = None

        while (len(self.get_page(total_pages, page_size)) != 0):
            total_pages += 1

        res['total_pages'] = total_pages

        return res


def index_range(page: int, page_size: int) -> Tuple:
    """
    The function that returns a tuple of size two
    containing start index and the end index.

    """
    first_index = 1 * (page * page_size) - page_size
    last_index = first_index + page_size

    result = (first_index, last_index)
    return result
