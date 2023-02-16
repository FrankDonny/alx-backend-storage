#!/usr/bin/env python3
from typing import Any, Callable, Optional
from uuid import uuid4

import redis


class Cache:
    """a cache class with redis client"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """store method"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Any:
        """Reading from Redis and recovering original type"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """calls the get method and converts the key to string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """calls the get method and converts the key to int"""
        return self.get(key, lambda x: int(x))


cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
