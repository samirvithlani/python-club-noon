a    for k in j:
        print("GDP: ",k)
        for l in k:
            print("GDP: ",l)
            if i == "IN":
                sum = sum + l
                ingdp.append(sum)
            elif i == "US":
                sum = sum + l
                usgdp.append(sum)
            elif i == "UK":
                sum = sum + l
                ukgdp.append(sum)        
        sum = 0        
        print("...........")

print("IN GDP: ",ingdp)
print("US GDP: ",usgdp)
print("UK GDP: ",ukgdp)