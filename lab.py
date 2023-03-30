# p6 (error code) - 9
# initialize the amount variable
try:
    f= open("demofile.txt")
    try:
        f.write("Lorum lpsum")
    except:
        print("Something went wrong while writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong while opening the file")
# output - Something went wrong while opening the file
#ans - File doesn’t exist 