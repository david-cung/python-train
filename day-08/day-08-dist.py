#dictionary

#cấu trúc dữ liệu cặp key và value

#cú pháp
new_dist =  {"key1": "value1", "key2": "value2"}

person = {"name": "Nhung", "age": 30}

#truy cập dist
# print(new_dist["key1"])
# print(new_dist["key2"])
# print(person["age"])

#Add new item
new_dist["key3"] = "value3"
#edit dist
new_dist["key1"] = "new_value"

# print(new_dist)

#loop in dist
# for key in new_dist:
#     print(f"Key: {key}, Value: {new_dist[key]}")
    
#another loop
for key, value1 in new_dist.items():
    print(f"{key}: {value1}")

