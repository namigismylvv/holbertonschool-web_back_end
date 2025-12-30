# Redis Basic

This project focuses on implementing Redis functionality in Python, using the `redis` module to handle basic operations and caching mechanisms.

## Tasks Overview

### 0. Writing strings to Redis
- Class implementation for storing data in Redis
- Using `uuid` for random generation of keys
- Method for storing input data in Redis

### 1. Reading from Redis and recovering original type
- Methods to convert data back to desired format
- Support for `str`, `bytes`, `int`, and `float` types
- Optional callable for type conversion

### 2. Incrementing values
- Implementation of counting decorator
- Track number of method calls in Redis

### 3. Storing lists
- Decorator for storing lists of inputs and outputs
- History tracking for function calls

### 4. Retrieving lists
- Function to display history of calls
- Shows inputs and outputs for tracked functions

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- First line of files should be `#!/usr/bin/env python3`
- Code should use `pycodestyle`
- All modules should have documentation
- All classes should have documentation
- All functions should have documentation
- Type annotations are required

## How to Use
```bash
# Install Redis
sudo apt-get -y install redis-server
pip3 install redis
```

## Authors
- Point L

## License
This project is licensed under the MIT License