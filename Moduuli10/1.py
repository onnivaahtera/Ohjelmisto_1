
class Elevator:
  def __init__(self, bottom: int, top: int):
    self.bottom = bottom
    self.top = top
    self.curr_floor = self.bottom 

  def floor_up(self):
    self.curr_floor += 1
    print(f"Floor {self.curr_floor}")


  def floor_down(self):
    self.curr_floor -= 1
    print(f"Floor {self.curr_floor}")
    

  def go_to_floor(self, floor: int):
    while(self.curr_floor != floor):
      if floor > self.top or floor < self.bottom:
        print(f"Floor {floor} does not exist")
        break
      if self.curr_floor < floor:
        self.floor_up()
      elif self.curr_floor > floor:
        self.floor_down()
      

def main():
  h = Elevator(1, 6)
  h.go_to_floor(6)
  h.go_to_floor(h.bottom)

if __name__=="__main__":
  main()