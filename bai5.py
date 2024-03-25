def dem_va_chen_so(nums, x):
    count = 0
    index = 0
    while index < len(nums):
        if nums[index] == x:
            count += 1
            nums.insert(index, x)
            index += 1
        index += 1
    return count
n=int(input("Nhap so phan tu:"))
danh_sach=[int(input("Nhap phan tu:")) for i in range(n)]
so_x=int(input("Nhap vao so x:"))
so_lan_xuat_hien = dem_va_chen_so(danh_sach, so_x)
print("Số lần xuất hiện của số", so_x, "trong danh sách:", so_lan_xuat_hien)
print("Danh sách sau khi chèn số", so_x, "vào trước các số bằng", so_x, "trong danh sách:", danh_sach)