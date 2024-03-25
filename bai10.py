def sap_xep(a):
	tang=sorted(a)
	giam=sorted(a,reverse=True)
	tang=tang[1:-1]
	giam=giam[1:-1]
	return tang,giam
n=int(input("Nhap so phan tu:"))
a=[int(input("Nhap phan tu:")) for i in range(n)]
tang,giam=sap_xep(a)
print("List tang dan:",tang)
print("List giam dan:",giam)
