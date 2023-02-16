#!/usr/bin/env python3
from typing import Any, Callable, Optional, Union
from uuid import uuid4

import redis


class Cache:
    """a cache class with redis client"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Union[str, bytes,
                                                             int, float, None]:
        """Reading from Redis and recovering original type"""
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """calls the get method and converts the key to string"""
        data = self._redis.get(key)
        return data.decode('utf-8')  # type: ignore

    def get_int(self, key: str) -> int:
        """calls the get method and converts the key to int"""
        data = self._redis.get(key)
        try:
            data = int(data)  # type: ignore
        except Exception:
            data = 0
        return data


cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
