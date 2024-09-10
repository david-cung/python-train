#vòng lặp: for --> chuỗi, danh sách, tuple, chuỗi số 
#vòng lặp: while -> lặp cho đến khi điều kiện = false.

# for variable in interable:
    #code
#interable : đối tượng mình muốn lặp qua (chuỗi, danh sách, tuple, chuỗi số )

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# var_range = range(10)
# for i in var_range:
#     print(i)
# start  -> stop -1
# numbers = [2, 6, 10]
# for number in numbers:
#     print(number)
# for i in range(2 , 11 , 4):
#     print(i)

# for letter in "12345678910":
#     print(letter)

#syntax
# while condition:
    #code

# i = 1
# while i:
#     print(i)
#     i +=1

# command = ""
# while command != "stop":
#     command = input("Please input command: ")

#dừng vòng lặp ngay lập tức: break
#bỏ qua lần lặp hiện tại chuyển sang vòng lặp tiếp theo -> continue

# item = [1,2,3,4,5]
# for i in range(10):
#     print(i)
#     if i == 5:
#         break

# item = [1,2,3,4,5]
# for i in item:
#     if i == 3:
#         continue
#     print(i)
#     print("tiep theo")
#     print("after continue")
    
matrix = [
    [1,2,3],
    [4,5,6]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()