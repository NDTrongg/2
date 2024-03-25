import math
def can_bac_ba(a):
	lst=[]
	for i in range(a+1):
		b=math.pow(i,1/3)
		if b==i:
			lst.append(i)
	return tuple(lst)
a=int(input("Nhap vao 1 so:"))
b=can_bac_ba(a)
print("cac so co the khai can bac ba:",b)