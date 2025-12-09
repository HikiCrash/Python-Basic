#2D좌표를 클래스로 표현
# 변수:x=0.0; y=0.0
# 리스트:[0.0, 0,0] (0.0, 0.0)
# 딕셔너리:{'x':0.0, 'y':0.0}
# x:3.0 y:-2.0 이동을 해야하는 상태
# pos['x'] += 3.0
# pos['y'] += -2.0


#class: 값(속성, 변수로 표현) + 기능(함수)
#class의 인스턴스가 갖고 있어야 하는
#필수 값(변수)는 __init__()에서 무조건 생성!
class Point:
    def __init__(self): # 생성자
        pass

    def test(self): # test 메서드
        self.x = 0.0 # 변수 x 생성

p = Point() # point 객체 생성
p.test() #Point.test(p), p.x가 생김.
print(p.x) # p.x 출력.


class Point2D: 
    def __init__(self): # 생성자에서 x,y 기본 변수 선언.
        self.x = 0.0
        self.y = 0.0
    
p = Point2D() # point2D 객체 생성
print(p.x, p.y)

class RectangleA:
    def __init__(self): # 사각형 기본 정보 생성.
        self.x = 0.0
        self.y = 0.0
        self.width = 0.0
        self.height = 0.0

r = RectangleA()
print(r.x, r.y, r.width, r.height)


#class == 자료형 (정의)
#object(instacne) = 자료형의 실체화.(실제로 존재하는 ...)

class RectangleB:
    def __init__(self):
        self.point = Point2D() # x,y 변수가 있는 클래스 사용.
        self.width = 1
        self.height = 0.0

r = RectangleB()
print(r.point.x, r.point.y, r.width, r.height)



class Point2D:
    def __init__(self, x=0.0, y=0.0): # 기본 값이 있는 생성자.
        self.x = x
        self.y = y
    
p = Point2D(100, 0) #사용자 지정 x, y
print(p.x, p.y)

p = Point2D() #기본값 x,y 사용
print(p.x, p.y)



class RectangleB:
    def __init__(self, x=0.0, y=0.0, w=0.0, h=0.0):
        self.point = Point2D(x, y)
        #self.point.x = x
        #self.point.y = y
        self.width = w
        self.height = h

r = RectangleB(x=1.1, y=2.0, w=1000.0, h=120.0)
print(r.point.x, r.point.y, r.width, r.height)

r = RectangleB()
print(r.point.x, r.point.y, r.width, r.height)



class Point2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def moveX(self, scaleX): # x 이동
        self.x += scaleX
        if self.x < 0.0: # x 0보다 작아지면 0 고정
            self.x = 0.0

    def moveY(self, scaleY): # y이 동
        self.y += scaleY
        if self.y < 0.0: # y 0보다 작아지면 0 고정
            self.y = 0.0            

    def moveXY(self, scaleX, scaleY): # x,y 동시 이동
        self.moveX(scaleX)
        self.moveY(scaleY)          

    
p = Point2D(100, 0) #사용자 지정 x, y
print(p.x, p.y)

p = Point2D() #기본값 x,y 사용
print(p.x, p.y)

#이동:x=> -13.0 y=> -5.9
p.x += -13.0
p.y += -5.9

print("p의 이동 1", p.x, p.y)

p.moveX(10)
p.moveY(10)
p.moveXY(10, 10)
print("p의 이동 2", p.x, p.y)

print(p) # p의 객체 가짜 메모리 주소 출력.


#print(): 콘솔화면에 '문자열' 출력;
#printf("hello world")
#printf(1); printf("%d", 1);

print(1) #"1"
print(1.1) #"1.1"
print("1.1")
print([1,2,3,])# "[1,2,3]"



class Point2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    #해당 [인스턴스]를 '문자열'로 만들어서 '반환'
    def __str__(self): # 출력될 때의 문자열 형태 지정.
        return f"({self.x}, {self.y})"

    def moveX(self, scaleX):
        self.x += scaleX
        if self.x < 0.0:
            self.x = 0.0

    def moveY(self, scaleY):
        self.y += scaleY
        if self.y < 0.0:
            self.y = 0.0            

    def moveXY(self, scaleX, scaleY):
        self.moveX(scaleX)
        self.moveY(scaleY)          

    
p = Point2D(100, 0) #사용자 지정 x, y
print(p.x, p.y)

p = Point2D() #기본값 x,y 사용
print(p.x, p.y)

#이동:x=> -13.0 y=> -5.9
p.x += -13.0
p.y += -5.9

print("p의 이동 1", p.x, p.y) # -13.0 -5.9

p.moveX(10)
p.moveY(10)
p.moveXY(10, 10)
print("p의 이동 2", p.x, p.y) # 10.0 14.1

print("p의 정보:", p) # (10.0, 14.1)



class RectangleB:
    def __init__(self, x=0.0, y=0.0, w=0.0, h=0.0):
        self.point = Point2D(x, y)
        #self.point.x = x
        #self.point.y = y
        self.width = w
        self.height = h

    def move_position(self, x , y): # 좌표 이동.
        self.point.moveXY(x,y)

    def change_size(self, w, h): # 값 덮어쓰기 코드.
        #값을 교체x, 가감o
        #self.width += w
        #if self.width < 0.0:
        #    self.width = 0.0

        #상황보고 바꾸기
        #if w >= 0.0:
        #    self.width = 0
            
        #바꿔놓고, 상황 봄...
        self.width = w 
        if self.width < 0.0:
            self.width = 0.0

        self.height = h
        if self.height < 0.0:
            self.height = 0.0    


r = RectangleB(x=1.1, y=2.0, w=1000.0, h=120.0)
print(r.point.x, r.point.y, r.width, r.height)

r = RectangleB()
print(r.point.x, r.point.y, r.width, r.height)