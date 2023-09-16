student={"name":"zhangsan","age":18,"sex":"1"}

for i in student.keys():
    print(i)

for i in student.values():
    print(i)

for i in student.items():
    print(i)

for key,values in student.items():
    print("key={},values={}".format(key,values))