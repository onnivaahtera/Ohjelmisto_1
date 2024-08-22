class Car:
  def __init__(self, register, top_speed, curr_speed=0, travel_distance=0):
    self.register = register
    self.top_speed = top_speed
    self.curr_speed = curr_speed
    self.travel_distance = travel_distance

car = Car("ABC-123", 142)
print(car.register, car.top_speed, car.top_speed, car.travel_distance)