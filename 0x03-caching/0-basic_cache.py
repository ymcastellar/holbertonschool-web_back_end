#!/usr/bin/python3
"""Basic dictionary"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Define BasicCache"""
    def put(self, key, item):
        """put item"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key:
            return self.cache_data.get(key)
        else:
            return None
