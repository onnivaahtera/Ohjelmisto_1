
from typing import List


class Elevator:
  def __init__(self, bottom_floor: int, top_floor: int) -> None:
    self.bottom_floor = bottom_floor
    self.top_floor = top_floor
    self.curr_floor = self.bottom_floor 

  def floor_up(self) -> None:
    self.curr_floor += 1
    print(f"Current floor {self.curr_floor}")


  def floor_down(self) -> None:
    self.curr_floor -= 1
    print(f"Current floor {self.curr_floor}")
    

  def go_to_floor(self, floor: int) -> None:
    while(self.curr_floor != floor):
      if self.curr_floor < floor:
        self.floor_up()
      elif self.curr_floor > floor:
        self.floor_down()

class Building:
  def __init__(self, bottom_floor: int, top_floor: int, elevators: int) -> None:
    self.bottom_floor = bottom_floor
    self.top_floor = top_floor
    self.elevators = [Elevator(self.bottom_floor, self.top_floor) for _ in range(elevators)] 

  def run_elevator(self, num_of_elevator: int, floor: int) -> None:
    if num_of_elevator < 0 or num_of_elevator >= len(self.elevators):
      print(f"\nElevator {num_of_elevator} does not exist")
      return
    print(f"\nElevator {num_of_elevator}")
    print("________________________\n")
    self.elevators[num_of_elevator].go_to_floor(floor)

  def fire_alarm(self) -> None:
    for elevator in self.elevators:
      elevator.curr_floor = self.bottom_floor



def main():
  building = Building(1, 10, 3)

  building.run_elevator(2, 7)
  building.run_elevator(1, 6)
  building.run_elevator(0, 6)
  
  building.fire_alarm()

if __name__=="__main__":
  main()