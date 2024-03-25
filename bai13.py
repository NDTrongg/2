def tach_danh_sach(am_duong):
	so_am=[]
	so_duong=[]
	for i in am_duong:
		if i>0:
			so_duong.append(i)
		else:
			so_am.append(i)
	return so_am,so_duong
n=int(input("Nhap so phan tu:"))
a=[int(input("Nhap phan tu:")) for i in range(n)]
so_duong,so_am=tach_danh_sach(a)
print("List chi co so am:",so_am)
print("List chi co so duong:",so_duong)
