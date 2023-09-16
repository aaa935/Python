student = {"name": "zhangsan", "age": 18, "sex": "1"}
print(student["name"])
student["name"] = "lisi"
print(student["name"])
print(student)
student["cat"] = "AA"
print(student)
del student['cat']
student['id'] = 10
print(student)
print("字典内键值对有{}".format(len(student)))
print(student.items())
print(student["id"])
student.clear()
student['aa'] = "aa"
print(student)
