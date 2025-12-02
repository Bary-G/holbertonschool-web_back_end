#!/usr/bin/env python3
"""
Module file with function 
"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Classes attributes initialization"""
        self.__dataset: List[List[str]] | None = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int), \
            "page and page_size must be integers"
        assert page > 0 and page_size > 0, \
            "page and page_size must be positive"

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes two integer arguments page and page_size
    and return a tuple of size two containing a
    start index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
