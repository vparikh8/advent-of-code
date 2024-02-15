from dataclasses import dataclass
from pathlib import Path
import time

INPUT_FILE = "input.txt"

@dataclass(frozen=True)
class Point():
    x: int
    y: int
    
@dataclass(frozen=True)
class Line():
    start: Point
    end: Point
    
class Grid():
    SAND_ORIGIN = Point(500,0)
    SAND_VECTORS = [Point(0,1), Point(-1, 1), Point(1, 1)]
    
    def __init__(self, lines: set[Line], floor=False) -> None:
        self.rock: set[Point] = self._get_rock(lines)
        self.sand = set()
        self.min_x = min(point.x for point in self.rock)
        self.max_x = max(point.x for point in self.rock)
        self.min_y = min(point.y for point in self.rock)
        self.max_y = max(point.y for point in self.rock)
        self._set_floor(floor)

    def _set_floor(self, floor: bool):
        self._floor = floor
        self._floor_y = self.max_y + 2
        self.max_y = self._floor_y        
        
    def _get_rock(self, lines: set[Line]):
        """ Process lines of rock. For each point in those lines, add a rock point to the set."""
        rock = set()
        for line in lines:
            x_start = min(line.start.x, line.end.x)
            x_end = max(line.start.x, line.end.x)
            y_start = min(line.start.y, line.end.y)
            y_end = max(line.start.y, line.end.y)
            rock.update({Point(x,y) for x in range(x_start, x_end+1)
                                    for y in range(y_start, y_end+1)})
        
        return rock
    
    def _is_empty(self, point: Point) -> bool:
        """ If this point is not rock or sand, return True. """
        if point not in self.rock and point not in self.sand:
            if self._floor:
                if point.y == self._floor_y:
                    return False
            return True
        
        return False
    
    def drop_sand(self) -> Point:
        """ Sand falls down until it reaches an obstacle.
        If it reaches an obstacle, it will they try to fall diagonally left, then diagonally right. """
        grain = Grid.SAND_ORIGIN
        falling = True
        while falling:
            for v in Grid.SAND_VECTORS:
                candidate = Point(grain.x + v.x, grain.y + v.y)
                if self._is_empty(candidate):
                    if not self._floor and candidate.y == self._floor_y:
                        return None
                    else: # there is a floor; expand the grid
                        self.min_x = min(self.min_x, grain.x - 1)
                        self.max_x = max(self.max_x, grain.x + 1)
                        self.min_y = min(self.min_y, grain.y)
                    
                    grain = candidate
                    self.min_y = min(self.min_y, grain.y)

                    break
            else: # Get here if all our fall positions are full
                falling = False

        self.sand.add(grain)
        if grain == Grid.SAND_ORIGIN:
            return None                  
        
        return grain
    
    def __str__(self) -> str:
        rows = []
        for y in range(self.min_y, self.max_y+1):
            row = f"{y:3d} "
            
            # print 1 col to either side
            for x in range(self.min_x-1, self.max_x+2):
                point = Point(x,y)
                if point in self.rock:
                    row += "#"
                    continue
                if self._floor and y == self._floor_y:
                    row += "#"
                    continue
                if point in self.sand:
                    row += "o"
                    continue
                row += "."
            
            rows.append(row)
            
        return "\n".join(rows)

def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()
        
    lines = process_lines(data)
    
    # Part 1
    grid = Grid(lines)
    
    adding_sand = True
    while adding_sand:
        adding_sand = grid.drop_sand()
    
    print(f"Part 1: resting grains={len(grid.sand)}")
    
    # Part 2
    grid = Grid(lines, floor=True)
    adding_sand = True    
    while adding_sand:
        adding_sand = grid.drop_sand()
        
    print(f"Part 2: resting grains={len(grid.sand)}")        
        
def process_lines(data):
    lines = set()
    for input_line in data:
        point_coords = input_line.split(" -> ")
        points = [Point(*map(int, coord.split(","))) for coord in point_coords]
        for i in range(1, len(points)):
            lines.add(Line(points[i-1], points[i]))
    
    return lines

if __name__ == "__main__":
    main()