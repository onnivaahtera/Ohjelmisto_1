from random import randint

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

class ElectricCar(Car):
  def __init__(self, register, top_speed, capacity):
    self.battery_capacity = capacity
    super().__init__(register, top_speed)

class GasolineCar(Car):
  def __init__(self, register, top_speed, tank_volume):
    self.tank_volume = tank_volume
    super().__init__(register, top_speed)
    
def main():
  electric_car = ElectricCar("ABC-15", 180, 52.5)
  gasoline_car = GasolineCar("ACD-123", 165, 32.3)

  electric_car.accelerate(130)
  gasoline_car.accelerate(130)

  electric_car.drive(3)
  gasoline_car.drive(3)

  print(f"{electric_car.distance_travelled}")
  print(f"{gasoline_car.distance_travelled}")

if __name__=="__main__":
  main()