#!/usr/bin/python3
""" MRU caching """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache"""
    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """ Return value stored in `key` key of cache.
            If key is None or does not exist in cache, return None."""
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
