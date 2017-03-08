class Car(object):
  num_of_wheels = 4
  speed = 0
  num_of_doors = 4
  def __init__(self,name="General",model="GM",car_type=None):
    self.car_type=car_type
    self.model=model
    self.name=name
  
    if name == "Porshe" or name == "Koenigsegg":
      self.num_of_doors = 2
    else:
      self.num_of_doors
      
    if car_type == "trailer":
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4    

  def is_saloon(self):
    return self.car_type != "trailer"   

  def drive(self, car_speed):
        if self.car_type == 'trailer':
            self.speed = car_speed * 11
        else:
            self.speed = 10 ** car_speed
        return self

