# p4 1 -WAP with function QnR(n,d) that returns quotient and reminder after dividing n by d.
def QnR(n, d):
    return [int(n/d),n%d]
print(QnR(7,4))