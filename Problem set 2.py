'''
#balance = 4842.00
currentBalance = balance #This will change
#annualInterestRate = .2
#monthlyPaymentRate = .04 
month = range(1,13)
totMinPayment = [0]

#balance = unpaidBalance + (interestRate/12)*unpaidBalance

for i in month:
    minPayment = currentBalance * monthlyPaymentRate
    totMinPayment.append(minPayment)
    unpaidBalance = currentBalance - minPayment
    interest = (annualInterestRate/len(month))*unpaidBalance
    currentBalance = unpaidBalance + interest
    print 'Month: ' + str(i)
    print 'Minimum monthly payment: %.2f' % minPayment
    print 'Remaining balance: %.2f' % currentBalance
print 'Total paid: %.2f' % sum(totMinPayment)
print 'Remaining balance: %.2f' % currentBalance
'''
'''
#balance = 3926.00
currentBalance = balance #This will change
#annualInterestRate = .2
#monthlyPaymentRate = .04 #This is what needs to be found
minPayment = 0
month = range(1,13)
totMinPayment = [0]

#balance = unpaidBalance + (interestRate/12)*unpaidBalance
while currentBalance >= 0:
    currentBalance = balance
    minPayment += 10
    for i in month:
        totMinPayment.append(minPayment)
        unpaidBalance = currentBalance - minPayment
        interest = (annualInterestRate/len(month))*unpaidBalance
        currentBalance = unpaidBalance + interest
        #print 'Month: ' + str(i)
        #print 'Minimum monthly payment: %.2f' % minPayment
        #print 'Remaining balance: %.2f' % currentBalance-
    #print 'Total paid: %.2f' % sum(totMinPayment)
    #print 'Remaining balance: %.2f' % currentBalance
print 'Lowest Payment: ' + str(minPayment)

'''

balance = 999999
currentBalance = balance #This will change
annualInterestRate = .18
monthlyPaymentRate = .04 #This is what needs to be found
monthlyInterestRate = annualInterestRate/12.0
epsilon = .01 #How far off I'm willing to be
minimum = balance/12
maximum = (balance*(1+monthlyInterestRate)**12)/12.0
iteration = 0

goalBalance = 0
midpoint = (minimum + maximum)/2.0
month = range(1,13)
totMinPayment = [0]

#balance = unpaidBalance + (interestRate/12)*unpaidBalance
while abs(currentBalance) >= epsilon:
    currentBalance = balance
    iteration += 1
    for i in month:
        unpaidBalance = currentBalance - midpoint
        interest = (annualInterestRate/len(month))*unpaidBalance
        currentBalance = unpaidBalance + interest
        #print 'Month: ' + str(i)
        #print 'Minimum monthly payment: %.2f' % minPayment
        #print 'Remaining balance: %.2f' % currentBalance-
    #print 'Total paid: %.2f' % sum(totMinPayment)
#    print 'maximum is: ' + str(maximum)
#    print 'midpoint is: ' + str(midpoint)
#    print 'Remaining balance: %.2f' % currentBalance
    if abs(currentBalance) <= epsilon:
        break
    elif currentBalance > 0:
        minimum = midpoint
    elif currentBalance < 0:
        maximum = midpoint
    midpoint = (minimum + maximum)/2.0
    
print 'Lowest Payment: %.2f' % midpoint
