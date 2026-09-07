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

        max_timestamp = 0
        for time in self.store[key]:
            max_timestamp = max(max_timestamp, time)
        
        return self.store[key][max_timestamp]