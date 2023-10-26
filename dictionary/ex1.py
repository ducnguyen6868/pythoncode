#xây dựng chương trình tra cứu từ điển
'''Yêu cầu : Cho phép người dùng thêm mới từ và ý nghĩa 
    tra cứu ý nghĩa của từ , sửa hoặc xóa một từ nào đó
'''
library=dict()
while(True):
    print("Lựa chọn yêu cầu :")
    print("Thêm từ vựng vào từ điển :0")
    print("Xóa từ vựng :1")
    print("Sửa từ vựng :2")
    print("Tra cứu từ vựng :3")
    print("Xóa toàn bộ từ điển :4")
    number=int(input())
    if number==0:
        word=input("Nhập từ vựng cần thêm:")
        meaning=input("Ý nghĩa của từ :")
        library.update({word : meaning})
        print("Thêm thành công !")
    elif number==1:
        word=input("Nhập từ cần xóa :")
        if word in library.keys():
            library.pop(word)
            print("Xóa thành công")
        else:
            print("Từ này không có trong từ điển")
        
    elif number==2:
        word=input("Nhập từ cần sửa :")
        if word in library.keys():
            word=input("Sửa thành :")
            meaning=input("Ý nghĩa của từ đó :")
            library.update({word : meaning})
            print("Sửa thành công !")
            
        else:
            print("Từ này không có trong từ điển")
    elif number==3:
        word=input("Nhập từ cần tra cứu :")
        if word in library.keys():
            print("Ý nghĩa :"+library[word])
        else:
            print("Từ này không có trong từ điển")
    elif number==4:
        library.clear()
        print("Xóa thành công toàn bộ từ điển")
    elif number==5:
        print(library)
    else:
        print("Vui lòng lựa chọn đúng !")