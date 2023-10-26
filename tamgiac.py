import math
# Nhập vào 3 điểm bất kỳ trên hệ trục tọa độ Oxy
# Kiểm tra xem 3 điểm này có tọa thành 1 tam giác không ?
xA=float(input("Nhập hoành độ điểm A"))
yA=float(input("Nhập tung độ điểm A"))
xB=float(input("Nhập hoành độ điểm B"))
yB=float(input("Nhập tung độ điểm B"))
xC=float(input("Nhập hoành độ điểm C"))
yC=float(input("Nhập tung độ điểm C"))
ab=math.sqrt(math.pow((xA-xB),2)+math.pow((yA-yB),2))
ac=math.sqrt(math.pow((xA-xC),2)+math.pow((yA-yC),2))
bc=math.sqrt(math.pow((xC-xB),2)+math.pow((yC-yB),2))
if (ab+ac)>bc and(ab+bc)>ac and (bc+ac)>ab:
    print("3 điểm vừa nhập tạo thành 1 tam giác")
    C=ab+bc+ac
    print("Chu vi của tam giác đó là ",C)
    C/=2
    S=math.sqrt(C*(C-ab)*(C-ac)*(C-bc))
    print("Diện tích của tam giác đó là ",S)
else:
     print("3 điểm vừa nhập không tạo thành 1 tam giác")
