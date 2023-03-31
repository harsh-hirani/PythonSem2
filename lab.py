# p6 (error code) - 14 - 7
# initialize the amount variable
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# ans -X is not declared so it will give NameError and resolve it in except block
# #out -Something went wrong \nThe 'try except' is finished