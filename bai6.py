lst=input("Nhap danh sach:").split()
tp=[]
for i in lst:
	if i.isupper():
		tp.append(i)
print("Cac chu so viet hoa:",tuple(tp))