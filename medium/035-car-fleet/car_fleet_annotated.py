class Solution:
    # Count how many groups of cars (fleets) arrive at target, given that a faster car
    # that catches a slower one ahead of it slows down and rides with it forever.
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair each car with its speed and order them from closest-to-target to farthest.
        # Processing front to back means every car we look at can only be blocked by cars already seen.
        cars = sorted(zip(position, speed), reverse=True)
        # One entry per fleet: the time its lead car reaches target. The top is the fleet
        # directly ahead of the car we are about to process.
        fleets = []
        for pos, spd in cars:
            # How long this car would take if nothing were in its way. Keep it as a float;
            # integer division would round two different times to the same value.
            time = (target - pos) / spd
            # If it takes longer than the fleet ahead, it never catches that fleet: new fleet.
            # If it takes less or equal time, it catches up before target and merges, so nothing
            # is pushed; the merged fleet keeps the slower leader's time, which is already on top.
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        # Each stack entry is one fleet crossing the line.
        return len(fleets)
