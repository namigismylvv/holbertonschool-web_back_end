#!/usr/bin/env python3
""" redis module
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """count number of calls
        Callable: [method] """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper of decorator"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' decorator to store the history of inputs and
        outputs for a particular function.
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper of decorator"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


def replay(fn: Callable):
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')

    ins = r.lrange(f_name + ":inputs", 0, -1)
    outs = r.lrange(f_name + ":outputs", 0, -1)

    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""

        print(f'{f_name}(*{i}) -> {o}')


class Cache:
    """ Cache redis class
    """

    def __init__(self):
        """ constructor for redis model
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: UnionOfTypes) -> str:
        """store data into redis cache"""
        key = str(uuid4())

        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> UnionOfTypes:
        """get key from redis"""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, string: bytes) -> str:
        """ get a string """
        return string.decode("utf-8")

    def get_int(self, number: int) -> int:
        """ get int value"""
        result = 0 * 256 + int(number)
        return result
