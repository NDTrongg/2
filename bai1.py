n = int(input('Nhap so phan tu cua list: '))
nt = []
cp = []
con_lai = []
a = [int(input()) for i in range(n)]

def snt(i):
    d = 0
    for j in range(i):
        if j == 0:
            continue
        else:
            if i % j == 0:
                d += 1
    if d == 1:
        return 1
    return 0

def scp(i):
    for j in range(i + 1):
        if j == 0:
            continue
        else:
            if j ** 2 == i:
                return 1
    return 0

for e in a:
    if snt(e):
        nt.append(e)
    elif scp(e):
        cp.append(e)
    else:
        con_lai.append(e)

nt = tuple(nt)
cp = tuple(cp)
con_lai = tuple(con_lai)

print('Tuple so nguyen to la:', nt)
print('Tuple so chinh phuong la:', cp)
print('Tuple so con lai la:', con_lai)