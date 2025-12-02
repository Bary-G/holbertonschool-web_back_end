#!/usr/bin/env python3
"""
Module file with function 
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Classes attributes initialization"""
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
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start:end]
    
    def get_hyper(self, page: int = 1, page_size: int = 10):
        """Returns a dictionary containing key-value pairs"""
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {"page_size": len(data),"page": page,"data": data,"next_page": next_page,"prev_page": prev_page,"total_pages": total_pages}


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes two integer arguments page and page_size
    and return a tuple of size two containing a
    start index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
