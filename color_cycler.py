

class Color_Cycler():
  def __init__(self, * colors):
      self.colors = []
      for color in colors:
          self.colors.append(color)

      self.cycle_count = 1
      self.color_change_frequency = 6

  def get_next_color(self):
      if self.cycle_count >= self.color_change_frequency:
          self.cycle_count = 1

      else:
          self.cycle_count += 1

      if self.cycle_count == self.color_change_frequency:
          next_color = self.colors.pop()
          self.colors.insert(0, next_color)
          return next_color

      else:
          return self.colors[0]