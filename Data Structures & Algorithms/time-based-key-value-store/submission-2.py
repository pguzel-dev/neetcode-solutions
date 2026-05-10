class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        bottom, top = 0, len(self.timeMap[key])-1
        curr_array = self.timeMap[key]
        curr_mood = ""
        while bottom <= top:
            mid = bottom + ((top - bottom) // 2)

            if curr_array[mid][0] == timestamp:
                return curr_array[mid][1]

            elif curr_array[mid][0] > timestamp:
                top = mid-1

            elif curr_array[mid][0] < timestamp:
                bottom = mid+1
                curr_mood = curr_array[mid][1]
            
        return curr_mood