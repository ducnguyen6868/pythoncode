# #là khối các lệnh trong hàm , chỉ được thực thi khi hàm đó được gọi
# '''  Viết hàm nhập vào 1 số và tính giai thừa của số đó
# '''
# def gt(n):
#     tich=1
#     for i in range(1,n+1):
#         tich*=i
#     return tich
# print(gt(10))
# '''Tìm ucln'''
# def ucln(a,b):
#     while(a!=b):
#         if a>b:
#             a=a-b
#         else:
#             b=b-a
#     return a
# print(ucln(1008,5))
# '''
#     Viết hàm nhập vào dãy số từ bàn phím và tính tổng dãy số đó
# '''
# def nhap(n):
#     list_number=list()
#     list_number=n.split(",")
#     tong=0
#     for i in list_number:
#         tong+=int(i)
#     return tong
# print(nhap("1,2,3,4,5,6"))
# '''Nhập vào một dãy số , cho biết dãy số đó có bao nhiêu phần tử chẵn , lẻ
#     , và sắp xếp chúng theo thứ tự
# '''
while(True):
    n=input("Nhập dãy số n:")
    break
def tinh(n):
    list=[]
    list_number=[]
    dem=0
    list=n.split(" ")
    for i in list:
        list_number.append(int(i))
        if int(i)%2==0:
            dem+=1
    print("Dãy số vừa nhập có "+str(dem)+" chữ sỗ chẵn")
    list_number.sort()
    print(list_number)
tinh(n)
