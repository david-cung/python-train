# List & Tuple

# List
#- Dữ liệu trong list có thể thay đổi được.

numbers = [1, 2, 3, 4, 5]
mixed = ['apple', 1, 'banana', 2]

#truy cập vào phần tử danh sách 
# print(fruits[2])
# print(fruits[1])
# print(fruits[-2])
# print(fruits[0])

#thay đổi phần tử trong danh sách
# fruits[0] = 'orange'

# print(fruits[0])

#----- phương thức làm việc với danh sách ----
#append():  Thêm một phần tử vào danh sách

# fruits.append('orange')
# fruits.append(1)
# print(fruits)

#insert(): ----Chèn vào một vị trí cụ thể theo chỉ định----
# print(fruits[1])
# fruits.insert(1, 'orange')
# print(fruits[1])

#remove() ----Xoá phần tử trong danh sách ----
# fruits.remove('banana')
#check index of item
# index = fruits.index('cherry')
# print(index)

#pop() --- xoá phần tử cuối cùng hoặc phần tử tại vị trí chỉ định ----

# fruits.pop() 
# fruits.pop(0)
# print(fruits)

#sort() -- sắp xếp danh sách
numbers = [3, 1, 5 , 9 , 0]
# numbers.sort(reverse = True)
# numbers.sort()
# print(numbers)
# fruits.sort()
# print(fruits)

#revert() --- đảo ngược danh sách ---
# numbers.reverse()


#len() ---trả về độ dài danh sách ---
# length = len(numbers)
# print(length)

# numbers.pop()
# length1 = len(numbers)
# print(length1)


#kết hợp vòng lặp và danh sách
# fruits = ['apple',  'cherry', 'banana']
# for fruit in fruits:
#     print(fruit)

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

#Danh sách lồng nhau
# matrix = [[2,3, 4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9,10]]
# a = [2,3, 4,5,6,7,8,9]
# b = [1,2,3,4,5,6,7,8,9,10]

# for i in a:
#     for j in b:
#         print(f"{i} * {j} = { i * j}")
# print(matrix[0])
# print(matrix[1])