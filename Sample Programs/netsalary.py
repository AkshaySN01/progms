base=float(input("Enter Basic Salary:"))
Allowances=float(input("Enter Allowances:"))
pf=float(input("Enter Provident Fund:"))
tax=float(input("Enter Income Tax:"))

Gross=base+Allowances-(pf+tax)
print("Net Salary is ",Gross)
