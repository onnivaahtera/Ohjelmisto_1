class Car:
  def __init__(self, register, top_speed):
    self.register = register
    self.top_speed = top_speed
    self.curr_speed = 0
    self.travel_distance = 0
    
  def accelerate(self, acceleration):
    self.curr_speed += acceleration
    if self.curr_speed < 0: 
      self.curr_speed = 0
    elif self.curr_speed > self.top_speed: 
      self.curr_speed = self.top_speed

  def drive(self, hours_driven):
    self.travel_distance += hours_driven * self.curr_speed
    
    
    

car = Car("ABC-123", 142)
print(car.register, car.top_speed, car.top_speed, car.travel_distance)

car.accelerate(60)
print(car.curr_speed)

car.drive(1.5)
print(car.travel_distance)