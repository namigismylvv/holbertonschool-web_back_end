#!/usr/bin/python3
""" LFU caching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache"""

    def __init__(self):
        """Initialize the LFUCache instance."""
        super().__init__()
        self.freq = {}  # Frequency count for each key
        self.usage = {}  # Usage order for tie-breaking

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        # Update the cache and frequency count
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                min_freq = min(self.freq.values())
                lfu_keys = [k for k, v in self.freq.items() if v == min_freq]
                # Break ties using the oldest usage
                lfu_key = min(lfu_keys, key=lambda k: self.usage[k])

                # Evict the LFU key
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                del self.usage[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Add the new key to the cache
            self.cache_data[key] = item
            self.freq[key] = 1

        # Update the usage timestamp for the key
        self.usage[key] = len(self.usage)

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None and key in self.cache_data:
            self.freq[key] += 1  # Increment frequency
            self.usage[key] = len(self.usage)  # Update usage timestamp
            return self.cache_data[key]
        return None
