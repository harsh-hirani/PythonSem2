# p4 4 -Formulate a problem definition of your own and demonstrate functions as objects.
def sum(props):
    sum = 0
    for s in props:
        sum += s
    return sum
def fact(n):
    if n<2:
        return 1
    return n*fact(n-1)
def QnR(n, d):
    return {'quotient':int(n/d),'reminder':n%d}
function_dict = {
    "sum":sum,
    "fact":fact,
    "qnr":QnR
}
print(type(function_dict["sum"]),function_dict["sum"]([1,2,3,4,5,6,7,8,9]))
print(type(function_dict["fact"]),function_dict["fact"](5))
print(type(function_dict["qnr"]),function_dict["qnr"](5,2))