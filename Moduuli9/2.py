class Car:
  def __init__(self, register, top_speed, curr_speed=0, travel_distance=0):
    self.register = register
    self.top_speed = top_speed
    self.curr_speed = curr_speed
    self.travel_distance = travel_distance
    
  def accelerate(self, speed):


car = Car("ABC-123", 142)

print(car.curr_speed)
car.accelerate(70)
print(car.curr_speed)
car.accelerate(-40)
print(car.curr_speed)
