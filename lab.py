# p6 (error code) - 11
# initialize the amount variable
x='hello'
if not type(x) is int:
    raise TypeError('Only integers are allowed')
# output - TypeError: Only integers are allowed
#ans - String is stored in x but condition check for it to be int and if not raise a type error with msg