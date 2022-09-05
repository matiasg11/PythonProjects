#Inputs: principal, rate, years to payback
#Calculate the monthly payment
#Show it to the user

def monthlyPayment():
    print("This will calculate the monthly payment for the loan. \n")
    principal = float(input("Input the loan amount: "))
    rate = float(input("Input the interest rate in percentage: "))
    years = float(input("Input the years to repay: "))

    monthlyRate = rate/(12*100)
    months = years*12
    payment = (principal * monthlyRate)/ (1-(1+monthlyRate)**(-months))

    print("Each month you'll pay %.2f" % payment)
monthlyPayment()