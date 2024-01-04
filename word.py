soz = input("So'z: ")
if len(soz) >= 10:
	print(soz[0],len(soz),soz[-1],sep='')
elif len(soz) >= 4:
	print(soz)
else:
	print("4 yoki 10dan katta so'z kiriting!!!")

