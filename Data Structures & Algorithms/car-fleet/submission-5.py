class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [[]] * len(position)

        for i in range(len(position)):
            fleets[i] = [position[i], speed[i]]
        
        fleets.sort(key=lambda item:item[0], reverse=True)
        
        times = []
        for car in fleets:
            time = (target - car[0]) / car[1]
            times.append(time)
        curr = 0
        res = 0
        for time in times:
            if time > curr:
                curr = time
                res += 1
        return res