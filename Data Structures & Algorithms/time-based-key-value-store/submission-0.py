class TimeMap:

    def __init__(self):
        self.store: dict[str, dict[int, str]] = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
            
        if timestamp in self.store[key]:
            return self.store[key][timestamp]

        l, r = 1, len(self.store[key])
        while l <= r:
            m = l + (r - l) // 2
            if m < timestamp:
                l = m + 1
            elif m > timestamp:
                r = m - 1
        return self.store[key][m]