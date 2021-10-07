UserInsert=input("Введите слово которое необходимо найти")
string = "Farukh Kutlikov Rakhmandzhanovich"
b = string.split()
i= 0
fl= False
while   i<len(b):
            if b[i]==UserInsert:
                print(b[i])
                fl=True
            i=i+1
if fl==False:
        print("Слово не найдено")