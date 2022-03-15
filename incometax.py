print("MERLIN BENEDICT")
print("To calculate income")
rate=2.2
standard_deduction=1000
dependent_deduction=3000
income=float(input("Enter the Gross income:"))
noofdependent=int(input("Enter the Number of dependent:"))
taxableincome=(income-standard_deduction-(dependent_deduction*noofdependent))
incometax=taxableincome*rate
print("Income tax=$",incometax)
