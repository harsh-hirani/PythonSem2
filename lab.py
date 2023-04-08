# p6 (error code) - 17 B
# initialize the amount variable
#OSError
import os
try :
    os.mkdir("new_dictionary")
except OSError as error:
    print("Error : ",error)

#out - Error : [WinError 183] Cannot create a file when that file already exists: 'new_dictionary'
