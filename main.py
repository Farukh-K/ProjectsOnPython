string = "Farukh Kutlikov Rakhmandzhanovich"
b = string.split()
i= 0
temp1 = b[0]
while   i<len(b):
            if b[i]<temp1:
                    temp1=b[i]
            i=i+1
print(temp1)