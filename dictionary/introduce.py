#Là từ điển lưu trữ các giá trị theo cấu trúc key : value
#các key không được trùng nhau
#Về cơ bản thì nó cũng giống như struct trong c++
infor={
    "firstName": "Nguyễn",
    "lastName":"Đức",
    "age":20 
}
# print(infor["firstName"])
# #Thêm giá trị vào dictionary
# infor.update({"location":"Vĩnh Phúc"})
# print(infor)
# #Thay đổi giá trị 
# infor["age"]=21
# print(infor)
# infor.update({"firstName":"Dương"})
# print(infor)
# #Xóa các phần tử trong dictionary
# infor.pop("lastName")
# print(infor)
# infor.popitem()#xóa đi cặp key: value cuối cùng 
# print(infor)
# del infor["age"]
# print(infor)
#del infor #Xóa luôn dictionary đó 
#infor.clear()#Xóa toàn bộ dữ liệu trong dictionary
print(infor)
for x in infor.keys():
    print(x) #in ra các giá trị keys tương ứng
for x in infor.values():
    print(x) #in ra các giá trị values tương ứng
for x,y in infor.items():
    print(x,y)
print("gdd" in infor.keys())
'''
    Nhập vào n , in ra kết quả theo dạng 1:2 ,2:4, 3:6,...,n:n*2
'''
# list_number=dict()# Khai báo một dictionary/thư viện rỗng
# n=int(input("Nhập n:"))
# for i in range(1,n+1):
#     list_number[i]=i*2
# print(list_number)