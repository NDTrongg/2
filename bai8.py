def kt_snt(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input("Nhap so duong:"))
lst=[]
for i in range(2,n+1):
    if n%i==0 and kt_snt(i):
        lst.append(i)
print(f"Thua so nguy to cua so {n} la {tuple(lst)}")