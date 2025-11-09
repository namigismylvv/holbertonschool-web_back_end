# Caching System

This repository provides several Python implementations of caching mechanisms, each demonstrating a different caching strategy.

## 📁 Files

### `0-basic_cache.py`
Implements a basic caching system using a simple Python dictionary.

### `1-fifo_cache.py`
Implements a FIFO (First-In, First-Out) caching algorithm where the oldest items are removed first.

### `2-lifo_cache.py`
Implements a LIFO (Last-In, First-Out) caching strategy where the most recently added items are discarded first.

## 🚀 Usage

Each caching class extends the `BaseCaching` class, which is defined in a separate module named `base_caching`.

### Example — BasicCache
```python
from 0-basic_cache import BasicCache

cache = BasicCache()
cache.put("A", "Hello")
print(cache.get("A"))  # Output: Hello
