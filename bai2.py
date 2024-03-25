n = int(input('Nhap so phan tu cua list: '))
a = [int(input()) for i in range(n)]
tang = []
giam = []


def SoDoiXung(n):
	temp = n
	sdx = 0
	while temp > 0:
		sdx = sdx * 10 + temp % 10
		temp //= 10
	if sdx == n:
		return True
	else:
		return False


for e in a:
	if SoDoiXung(e):
		tang.append(e)
	else:
		giam.append(e)

tang.sort()
giam.sort(reverse=True)

print('Danh sach sau khi sap xep tang la:', tang)
print('Danh sach sau khi sap xep giam la:', giam)