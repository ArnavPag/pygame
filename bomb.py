from game_object import GameObject
from random import randint, choice

class Bomb(GameObject):
  def __init__(self):
    super(Bomb, self).__init__(0, 0, 'images/bomb.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.x > 564 or self.x < -64 or self.y > 564 or self.y < -64:
      self.reset()

  def reset(self):
    direction = randint(1, 4)
    coordinates = [93, 218, 343]

    if direction == 1:
      self.x = 564
      self.y = choice(coordinates)
      self.dx = ((randint(25, 200) / 100) + 1) * - 1
      self.dy = 0

    elif direction == 2:
      self.x = -64
      self.y = choice(coordinates)
      self.dx = (randint(25, 200) / 100) + 1
      self.dy = 0

    elif direction == 3:
      self.x = choice(coordinates)
      self.y = -64
      self.dx = 0
      self.dy = (randint(25, 200) / 100) + 1

    else:
      self.x = choice(coordinates)
      self.y = 564
      self.dx = 0
      self.dy = ((randint(25, 200) / 100) + 1) * -1
    