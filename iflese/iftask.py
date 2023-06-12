income = int(input("Enter your income: "))
pt = 200
pfper = 10
taxreachpoint = 700000
tax =0
taxper = 10
aftertaxincome =0

netincome = income - pt
print("Your net income is: ", netincome)
netincome1 = netincome - (netincome * pfper / 100)
print("Your net income after PF is: ", netincome)
totalpf = netincome - netincome1
yearlyincome = netincome1 * 12
print("Your yearly income is: ", yearlyincome)

if yearlyincome>taxreachpoint:
    tax = yearlyincome * taxper / 100
    print("Your tax is: ", tax)
    aftertaxincome = yearlyincome - tax
else:
    print("You are not eligible for tax")
    aftertaxincome = yearlyincome


print("Your after tax income is: ", aftertaxincome)        

if aftertaxincome> 100000:
    print("You are eligible for loan")
    
    if aftertaxincome> 150000:
        print("You are eligible for 2 wheeler loan")
    
    if aftertaxincome> 300000:
        print("You are eligible for 4 wheeler loan")    
        
    if aftertaxincome> 500000:
        print("You are eligible for personal loan")
    
    if aftertaxincome> 1000000:
        print("You are eligible for home loan")    

else:
    print("You are not eligible for loan")
    
    if aftertaxincome> 50000:
        print("You are eligible for eligible for credit card")        




