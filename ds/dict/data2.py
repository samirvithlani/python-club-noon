data ={'countries':["India","USA","UK","Australia","Canada"],'states':["MH","Taxas","London","Sydney","Ontario"]}
print(data)

x = data.get('countries')
print(x)

data.get('countries').append("Japan")


for i,j in data.items():
    print(i)
    for k in j:
        print(k)
    
    print("**************")    
    
