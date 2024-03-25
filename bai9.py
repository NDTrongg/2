def chia_het_cho2_va3(x,y):
	lst=[]
	for i in range(x,y+1):
		if i%2==0 and i%3==0:
			lst.append(i)
	return tuple(lst)
x=int(input("Nhap vao 1 so:"))
y=int(input("Nhap vao 1 so:"))
a=chia_het_cho2_va3(x,y)
print("Cac so vua chia het cho 2 vua chia het cho 3",a)