#!/usr/bin/env python3
"""Defines LFUCache class"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implement LFUCache class"""

    def __init__(self):
        super().__init__()
        self.lfu = []

    def put(self, key, item):
        """Add an item to the cache with LFU eviction policy"""
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.update_frequency_and_move_to_end(key)
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq = min(self.lfu, key=lambda x: x[1])

            del self.cache_data[min_freq[0]]
            self.lfu.remove(min_freq)
            print(f"DISCARD: {min_freq[0]}")

        self.cache_data[key] = item
        self.lfu.append((key, 1))

    def get(self, key):
        """Retrieve an item from the cache"""
        value = self.cache_data.get(key)

        if value:
            self.update_frequency_and_move_to_end(key)

        return value

    def update_frequency_and_move_to_end(self, key):
        """
        Update frequency of the key and
        move its corresponding tuple to the end
        """
        for i, (existing_key, frequency) in enumerate(self.lfu):
            if existing_key == key:
                self.lfu[i] = (key, frequency + 1)
                self.lfu.append(self.lfu.pop(i))
                break
