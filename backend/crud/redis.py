import redis


class RedisCrud:
    def __init__(self):
        self.connect = redis.Redis(host='redis', port=6379, db=0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connect.close()

    def get(self, key):
        return self.connect.get(key)

    def set(self, key, value):
        return self.connect.set(key, value)

    def delete(self, key):
        return self.connect.delete(key)
