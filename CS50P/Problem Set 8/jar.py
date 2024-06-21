def main():
    jar = Jar()
    print(jar)
    """jar.deposit(1)
    print(jar)
    jar.withdraw(2)
    print(jar)"""


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 5

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0 or not isinstance(n, int):
            raise ValueError("Deposit must be a non-negative integer.")
        if self._size + n > self._capacity:
            raise ValueError("Exceed jar capacity.")
        self._size += n

    def withdraw(self, n):
        if n < 0 or not isinstance(n, int):
            raise ValueError("Deposit must be a non-negative integer.")
        if self._size < n:
            raise ValueError("Not enough cookies in the jar.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    

if __name__ == "__main__":
    main()