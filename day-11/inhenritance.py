class Animal:
    def __init__(self, name, color):
        #Sử dụng 2 dấu gạch dưới để định nghĩa thuộc tính private
        self.__name = name
        
        #Sử dụng 1 dấu gạch dưới để định nghĩa thuộc tính protected
        self._color = color
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
class Dog(Animal):
    def make_sound(self):
        print(f"{self._color} is barking.")
        
dog = Dog("Buddy", "Black")
dog.make_sound()
