from dataclasses import dataclass
from pathlib import Path
import re
import functools
import time

INPUT_FILE = "input.txt"

@dataclass(frozen=True)
class Valve():
    id: str
    rate: int
    leads_to: set[str]
        
def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()
        
    valves = parse_input(data)

    @functools.cache
    def calc_max_relief(opened, mins_remaining, curr_valve_id, elephant=False):
        # Base case
        if mins_remaining <= 0:
            if elephant:
                return calc_max_relief(opened, 26, "AA")
            else:
                return 0

        most_relief = 0
        current_valve = valves[curr_valve_id]
        for neighbour in current_valve.leads_to:
            # Recurse for each neighbouring position
            most_relief = max(most_relief, calc_max_relief(opened, mins_remaining - 1, neighbour, elephant))

        # We only want to open valves that are closed, and where flow rate is > 0
        if curr_valve_id not in opened and current_valve.rate > 0 and mins_remaining > 0:
            opened = set(opened)
            opened.add(curr_valve_id)
            mins_remaining -= 1
            total_released = mins_remaining * current_valve.rate

            for neighbour in current_valve.leads_to:
                # Try each neighbour and recurse in. Save the best one.
                most_relief = max(most_relief, 
                           total_released + calc_max_relief(frozenset(opened), mins_remaining - 1, neighbour, elephant))

        return most_relief

    print(f"Part 1: {calc_max_relief(frozenset(), 30, 'AA')}")
    print(f"Part 2: {calc_max_relief(frozenset(), 26, 'AA', True)}")

def parse_input(data) -> dict[str, Valve]:
    pattern = re.compile(r"Valve ([A-Z]{2}) has flow rate=(\d+);.+[valve]s? (.+)")
    valves = {}
    for line in data:
        valve, rate, leads_to = pattern.findall(line)[0]
        valves[valve] = Valve(valve, int(rate), {x.strip() for x in leads_to.split(",")})
    
    return valves

if __name__ == "__main__":
    main()