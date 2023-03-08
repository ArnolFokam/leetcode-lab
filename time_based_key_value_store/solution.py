class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key] = self.data.get(key, [])
        self.data[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        data = self.data.get(key, [])
        res = ""
        l, r = 0, len(data) - 1

        while l <= r:
            m = (l + r) // 2

            if data[m][1] < timestamp:
                # we know that the timespan is greater than mid
                # therefore mid is the greatest number know to
                # be less than timespan. There might be others
                # but we haven't yet encouterd them
                res = data[m][0] 
                l = m + 1
            elif data[m][1] > timestamp:
                r = m - 1
            else:
                return data[m][0]

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)