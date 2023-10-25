import math
print(math.pi)
'''(range(0,2000))
a=b=c="Say my name"
print(a)
for k in range(1000,2000):
    if(k%5==0&k%9==0):
        print(k)
'''
#tim so nguye to 
#kieu du lieu
# a=5
# b=5
# c=a/b
# d="343"
# print(c)
# print("Kieu du lieu cua a", type(a))
# print("Kieu du lieu cua b", type(b))
# print("Kieu du lieu cua c", type(c))
# print(a+int(d))
# #các phép toán cơ bản 
# a=int(input("Nhập a:"))
# b=int(input("Nhập b:"))
# print("{0}+{1}={2}".format(a,b,a+b))
# print("{0}-{1}={2}".format(a,b,a-b))
# print("{0}*{1}={2}".format(a,b,a*b))
# print("{0}/{1}={2}".format(a,b,a/b))
# print("{0}//{1}={2}".format(a,b,a//b))
# print(a>b)
#Các hàm toán tử
'''print(math.ceil(a))
print(math.floor(a))
print(math.fabs(a))
b=4
print(pow(math.ceil(a),b))
c=8
print(math.log(10,100))'''
#giải phương trình bậc 2
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
c=int(input("Nhap c:"))
delta=b**2-4*a*c
delta=math.sqrt(delta)
if(delta<0):
    print("Phương trình vô nghiệm")
elif(delta==0):
    print("Phương trình có nghiên duy nhất x=",-b/(2*a))
else:
    x1=(-b+delta)/(2*a)
    x2=(-b-delta)/(2*a)
    print("Phương trình có 2 nghiệm phân biệt ")
    print("x1={0} và x2={1} ".format(x1,x2))
