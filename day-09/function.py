#syntax
def functionName(parameter1, parameter2):
    #content
    return parameter1

def total(parameter1, parameter2):
    print(f"param1: ", parameter1, "param2: ", parameter2)
    a = str(parameter1) + parameter2
    return a

#call function
# totalParameter = total(1, "nhung") #1,2 doi so
# print(totalParameter) 

def printString():
    print("Hello, World!")
    print("================================")
    print("This is a function")
    a = 5 + 7
    print(a)
    return a

# string = printString()
# print(string)
# printString()

#default parameters 
def printStringWithDefaultValue(name="Nhung"):
    print(f"Hello, {name}!")

# printStringWithDefaultValue()
# printStringWithDefaultValue("Python")

#tham so tuy y 
# *args: truyền số lượng đối số không xác định dưới dạng tuple
# **kwargs: truyền các đối số từ khoá không xác định dưới dạng dictionary

def sum(*numbers):
    total = 0
    for number in numbers:
        print(f"{number}")
        total += number
    return total

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# total = sum(*a)
# print(total)

def information(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# information(name="Nhung", age=30, address="QN", contry= "VN")
dist= {"name": "Nhung", "age": 30}

# information(**dist)

#lambda function
#function no name, basic function

nhan_doi = lambda x: x * 2
# print(nhan_doi(5))


#nested function
def tinh_bieu_thuc(number1):
    def phep_cong(number2):
        return number1
    return phep_cong

# print(tinh_bieu_thuc(5)(3))

def so_chan(a):
    if a % 2 ==0:
        return "day la so chan"
    else:
        return "day la so le"

number = input("Input number: ")
result = so_chan(int(number))

print(result)

