# p6 (error code) - 6
# initialize the amount variable
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")



# output - Variable x is not defined
#ans - As above it is a NameError so it will execute that block