class Car:
  def __init__(self, register, top_speed):
    self.register = register
    self.top_speed = top_speed
    self.curr_speed=0
    self.travel_distance=0

car = Car("ABC-123", 142)
print(car.register, car.top_speed, car.top_speed, car.travel_distance)