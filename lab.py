# p4 1 -WAP with function QnR(n,d) that returns quotient and reminder after dividing n by d.
def QnR(n, d):
    return {'quotient':int(n/d),'reminder':n%d}
print(QnR(int(input('Numerator: ')),int(input('Denominator: '))))