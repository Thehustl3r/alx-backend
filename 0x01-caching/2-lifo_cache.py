#!/usr/bin/python3
"""1-fifo_cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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

        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]
        self.cache_data[key] = item

        return self.cache_data

    def get(self, key, ):
        """method that get data in the caching system"""
        if key is None:
            return None

        try:
            self.cache_data[key]
        except KeyError:
            return None

        return self.cache_data[key]
