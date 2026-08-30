class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        time_stack = []
        pos_speed = [list(item) for item in zip(position, speed)]
        pos_speed.sort(key=lambda pos: pos[0], reverse=True)
        for pair in (pos_speed):
            time = (target - pair[0]) / pair[1]
            if time_stack and time_stack[-1] >= time:
                continue
            time_stack.append(time)
            res += 1
        return res