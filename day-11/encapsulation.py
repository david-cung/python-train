class Animal:
    def __init__(self, name, color):
        #Sử dụng 2 dấu gạch dưới để định nghĩa thuộc tính private
        self.__name = name
        
        #Sử dụng 1 dấu gạch dưới để định nghĩa thuộc tính private
        self._color = color
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name


dog = Animal("Buddy", " Black")

print(dog.__name)
print(dog.get_name())