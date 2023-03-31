# p6 (error code) - 15 - 9
# initialize the amount variable
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# ans -File doesn’t exist 
#out -Something went wrong when opening the file