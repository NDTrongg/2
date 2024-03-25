import math
def chen_so_0(list_so_nguyen):
	for i in range(len(list_so_nguyen)):
		if math.isqrt(list_so_nguyen[i])**2== list_so_nguyen[i]:
			list_so_nguyen.insert(i,0)
			#i+=1
	return list_so_nguyen
n=int(input("Nhap so phan tu:"))
a=[int(input("Nhap phan tu:")) for i in range(n)]
a=chen_so_0(a)
print("List sau khi chen so 0 vao truoc cac so chinh phuong",a)