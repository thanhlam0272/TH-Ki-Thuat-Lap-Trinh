import math
def tinh(r,h): 
    sday=r**2*math.pi 
    sxq=2*r*h*math.pi
    v=sday*h
    if r<0 or h<0:
        print "Ban nhap khong hop le"
    else: 
        print "Dien tich day la:",sday
        print "Dien tich xung quanh la:",sxq
        print "The tich la:",v
if __name__=="__main__": 
    r=float(raw_input("Nhap ban kinh: "))
    h=float(raw_input("Nhap chieu cao: "))
    tinh(r,h)
