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
    
    
def create_cars():
    car_list = []
    [car_list.append(Car(f"ABC-{i + 1}", randint(100, 200))) for i in range(10)]
    return car_list
    
def main():
  car_list = create_cars()

  while True:
    for car in car_list:
      car.accelerate(randint(-10, 15))
      car.drive(1)
      if car.distance_travelled > 10000:
        break 
    else: 
      continue
    break
  for car in car_list:
    print(f"Car({car.register}, Max Speed: {car.top_speed} km/h, Distance Travelled: {car.distance_travelled} km")



if __name__=="__main__":
  main()