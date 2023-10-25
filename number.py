#in ra toàn bộ số chẵn từ 100 đến 1000
# for i in range(100,1000):
#     if i%2==0:
#         print(i)
#Nhập vào 1 số và in ra giai thừa của số đó
## C1: Sử dụng vòng lặp for
# n=int(input("Nhập n:"))
# k=1
# for i in range(1,n+1):
#     k*=i
# print("{0}!={1}".format(n,k))
## C2 Sử dụng đệ quy
n=int(input("Nhập n:"))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print("{0}!={1}".format(n,fact(n)))
