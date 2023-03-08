# House down payment planner 
totalValue = float(input('Total Value: '))
portion_down_payment = 0.25
current_savings = float(input('Current Saving: '))
r = 0.04
annual_salary = float(input('Annual salary: '))
portion_saved = float(input('portion of your salary: '))/100
months = 0
savings = current_savings
print('-------------')
print('Your target is: ',totalValue*portion_down_payment)
if savings >= totalValue*portion_down_payment:
    print('You already have enough money to buy a house :)')
else:
    while savings<totalValue*portion_down_payment:
        current_savings = current_savings + current_savings*r/12
        savings = savings + current_savings*r/12 + annual_salary*portion_saved/12
        months = months + 1
        print("Month: ",months)
        print('savings: ' ,savings,' { +',(current_savings*r/12+annual_salary*portion_saved/12),' }')

        print("Congratulation After ",months," months you can buy your house")
