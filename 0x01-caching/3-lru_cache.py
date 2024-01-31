#!/usr/bin/python3
"""1-fifo_cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ BaseCahe defines:
      - is a caching systems that inherints from BaseCaching class
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        BaseCaching.__init__(self)
        self.usage_order = []

    def put(self, key, item):
        """method that insert new data in the caching system"""

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                least_used_key = self.usage_order.pop(0)
                print(f"DISCARD: {least_used_key}")
                del self.cache_data[least_used_key]
            self.cache_data[key] = item
            self.usage_order.append(key)

        return self.cache_data

    def get(self, key, ):
        """method that get data in the caching system"""
        if key is None:
            return None

        try:
            self.cache_data[key]
        except KeyError:
            return None
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
