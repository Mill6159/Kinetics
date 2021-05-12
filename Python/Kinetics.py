# General description of script
# List details here




# Import modules



# Define classes

class Main:
  '''
  This will be our main "SuperClass"
  '''
  def __init__(self, name, temp):
    self.name = name
    self.temp = temp
    print("MAIN", name)


# Main Calculation class below

class Calculations(Main):
  '''
  This class will inherit all of the variables of the "Main" class
  BUT also be able to take it's own variables as inputs
  '''
  def __init__(self, name, temp, km, vmax):
    self.km = km
    self.vmax = vmax
    Main.__init__(self, name, temp)

  def returnVariables(self):
    print('List of variables:', self.name, self.vmax)

# Plotting Class

# Export Class/File Parser

# Test code here!

calcs = Calculations(
                     name = 'Tom', 
                     temp = "20", 
                     km=1, 
                     vmax=2
                     )