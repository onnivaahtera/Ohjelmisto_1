from random import randint
from typing import List

class Car:
  def __init__(self, register, top_speed):
    self.register = register
    self.top_speed = top_speed
    self.curr_speed = 0
    self.distance_travelled = 0

  def accelerate(self, acceleration):
    self.curr_speed += acceleration
    if self.curr_speed < 0: 
     self.curr_speed = 0
    if self.curr_speed > self.top_speed: 
      self.curr_speed = self.top_speed

  def drive(self, hours_driven):
    self.distance_travelled += hours_driven * self.curr_speed

  def __repr__(self):
    return f"Car({self.register}, Max Speed: {self.top_speed} km/h, Distance Travelled: {self.distance_travelled} km, Car({self.curr_speed}))"
    
    
class Race:
  def __init__(self, name: str, distance: int, cars: List) -> None:
    self.name = name
    self.distance = distance
    self.cars = cars

  def hour_passes(self) -> None:
        for car in self.cars:
          car.accelerate(randint(-10, 15))
          car.drive(1)

  def print_status(self) -> None:
    for car in self.cars:
      print(f"Car({car.register}, Max Speed: {car.top_speed} km/h, Distance Travelled: {car.distance_travelled} km")
    print("\n")
  def race_finished(self) -> bool:
    for car in self.cars:
      if car.distance_travelled >= self.distance:
        return True
    return False

def main():
  race = Race("Grand Demolition Derby", 8000, [(Car(f"ABC-{i + 1}", randint(100, 200))) for i in range(10)])
  timer = 0
  while True:
    race.hour_passes()
    timer += 1
    if timer % 10 == 0:
      race.print_status()
    if race.race_finished() == True:
      race.print_status()
      break


if __name__=="__main__":
  main()