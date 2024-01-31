#!/usr/bin/python3
"""0-basic_cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BaseCahe defines:
      - is a caching systems that inherints from BaseCaching class
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        """method that insert new data in the caching system"""

        if key is None or item is None:
            return

        self.cache_data[key] = item

        return self.cache_data

    def get(self, key, ):
        """method that get data in the caching system"""

        try:
            self.cache_data[key]
        except IndexError:
            return None

        return self.cache_data[key]
