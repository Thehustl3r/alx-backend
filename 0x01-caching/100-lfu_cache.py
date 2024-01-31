#!/usr/bin/python3
"""1-fifo_cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ BaseCahe defines:
      - is a caching systems that inherints from BaseCaching class
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        BaseCaching.__init__(self)
        self.usage_order = {
            'not_accessed': [],
            'accessed': []
        }

    def put(self, key, item):
        """method that insert new data in the caching system"""

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            # self.usage_order.remove(key)
            # self.usage_order.append(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if len(self.usage_order['not_accessed']) != 0:
                    least_used_key = self.usage_order['not_accessed'].pop(0)
                else:
                    least_used_key = self.usage_order['accessed'].pop(0)

                print(f"DISCARD: {least_used_key}")
                del self.cache_data[least_used_key]
            self.cache_data[key] = item
            least_used_key = self.usage_order['not_accessed'].append(key)
            # self.usage_order.insert(0, key)

        return self.cache_data

    def get(self, key, ):
        """method that get data in the caching system"""
        if key is None:
            return None

        try:
            self.cache_data[key]
        except KeyError:
            return None
        if key in self.usage_order['accessed']:
            self.usage_order['accessed'].remove(key)
            self.usage_order['accessed'].append(key)

        else:
            self.usage_order['not_accessed'].remove(key)
            self.usage_order['accessed'].append(key)

        return self.cache_data[key]
