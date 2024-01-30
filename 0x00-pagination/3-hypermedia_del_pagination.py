#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        the funciton that takes the starting index and page_size
        and return the information of dara
        """
        dataset = self.__indexed_dataset
        res = {
            'index': 0,
            'data': [],
            'page_size': 0,
            'next_index': 0
        }
        res['index'] = index

        try:
            assert index in dataset.keys(), "index must be in a valid range"

        except AssertionError as e:
            if index > len(dataset):
                print("AssertionError raised when out of range")
                return
            else:

                index += 1

        res['page_size'] = page_size
        next_index = index + page_size
        res['next_index'] = next_index
        res['data'] = [dataset[i] for i in range(index, next_index)]

        return res
