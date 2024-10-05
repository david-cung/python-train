#hướng đối tượng : xây dựng đối tượng (dữ liệu, hành vi, đặc điểm, đặc tính đối tượng)

#car, people, computer

#refactor -->> maintain
#cleanCode ---> parameter's names 

#Class: -> property + function
#Object: -> 
#1. Encapsulation(Đóng gói): Giấu đi các chi tiết bên trong của đối tượng và chỉ cho phép tương tác thông qua các phương thức. Điều này bảo vệ dữ liệu và kiểm soát cách dữ liệu được thay đổi.
#2. Inheritance(Kế thừa): Cho phép một lớp con thừa hưởng các thuộc tính và phương thức từ một lớp cha.
#3. Polymorphism(Đa hình): Cho phép một phương thức hoặc thuộc tính có thể có nhiều cách hành xử khác nhau dựa trên ngữ cảnh.
#4. Abstraction(Trừu tượng):Ẩn đi những chi tiết phức tạp và chỉ hiển thị những chức năng quan trọng. 

#loại của thuộc tính: public, private, protected
class Animal:
    #Constructor để khởi tạo đối tượng
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    #Phương thức mô tả hành động 
    def make_sound(self):
        print(f"{self.name} is making a sound")
        
#truy cập thuộc tính 
dog = Animal("Buddy1", "Black")

print(dog.name)
print(dog.color)

#Gọi phương thức
dog.make_sound()

