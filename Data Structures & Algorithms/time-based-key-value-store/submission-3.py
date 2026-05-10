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

        curr_array = self.timeMap[key]

        # Too early for any stored value
        if timestamp < curr_array[0][0]:
            return ""

        # At or after the latest stored value
        if timestamp >= curr_array[-1][0]:
            return curr_array[-1][1]

        bottom, top = 0, len(curr_array) - 1
        curr_mood = ""

        while bottom <= top:
            mid = bottom + ((top - bottom) // 2)

            if curr_array[mid][0] == timestamp:
                return curr_array[mid][1]

            elif curr_array[mid][0] > timestamp:
                top = mid - 1

            else:
                curr_mood = curr_array[mid][1]
                bottom = mid + 1

        return curr_mood