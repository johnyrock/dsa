class Solution:
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = []  # arrival time of the lead car of each fleet, front-most first
        for pos, spd in cars:
            time = (target - pos) / spd
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)
