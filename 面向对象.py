# class A():
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
#     def c(self):
#         return ("x={}y={}".format(self.x,self.y))
#
# a=A(1,2)
# print(a.c())
# *****************************
# class A():  # 构造类
#     def b(self, x, y):  # self是一个传递信息的参数，不用显式传递参数
#         self.x = x
#         self.y = y
#
#     def c(self):
#         return ("x={},y={}".format(self.x, self.y))
#
#
# a = A()
# a.b(1, 2)
# print(a.c())
# ***********************************
# class I():
#     def b(self, x, y):
#         self.x = x
#         self.y = y
#
#     def c(self):
#         # print ("x={},y={}".format(self.x, self.y))
#         return "x={},y={}".format(self.name, self.blood)


# a = I()  # 类实例化
# a.b(1, 2)  # 用a给a()里面的方法b赋值，并用self传递参数，self.x=x就是把x放在self下面使得可以传递给这个类里面其他的方法
# print(a.c())
# b=I()
# b.b(12,22)
# print(b.c())
# **************
# c=I()
# c.name="zhangsan"
# c.blood=1000
# print(c.c())


#
# class Hero():
#     def ii(self, name, hp, atk):
#         self.hp = hp
#         self.atk = atk
#         self.name=name
#
#     def name1(self):
#         print("名字：{}".format(self.name))
#
#     def hp1(self):
#         print("血量：{}".format(self.hp))
#
#     def atk1(self):
#         print("攻击力：{}".format(self.atk))
#
#     def zong(self):
#         print("名字：{}".format(self.name))
#         print("血量：{}".format(self.hp))
#         print("攻击力：{}".format(self.atk))
#
# aa=Hero()
# aa.name=1
# aa.atk=1000
# aa.hp=5000
# aa.zong()


# class Hero():
#     def ii(self, name, hp, atk):
#         self.hp = hp
#         self.atk = atk
#         self.name()
#
#     def name1(self):
#         print("名字：{}".format(self.name))
#
#     def hp1(self):
#         print("血量：{}".format(self.hp))
#
#     def atk1(self):
#         print("攻击力：{}".format(self.atk))
#
#
# aa = Hero()
# aa.ii(2500, 100, 1000)
# aa.name1()
# aa.hp1()
# aa.atk1()


# class Hero():
#     def ii(self, name, hp, atk):
#         self.hp = hp
#         self.atk = atk
#         self.name=name
#
#
#     def sc(self):
#         print("名字：{}".format(self.name))
#         print("血量：{}".format(self.hp))
#         print("攻击力：{}".format(self.atk))
#         print(("**********************"))
#
#
# aa = Hero()
# aa.ii(1, 100, 1000)
# aa.sc()
# bb=Hero()
# bb.ii(12,1222,212)
# bb.sc()
#
# class Hero():
#     def __init__(self,name,hp,atk):
#         self.name=name
#         self.hp=hp
#         self.atk=atk
#     def sc(self):
#
#         print("名字：{}".format(self.name))
#         print("血量：{}".format(self.hp))
#         print("攻击力：{}".format(self.atk))
#         print(("**********************"))
#
#     def __str__(self):
#         return "数据：{},{},{}".format(self.name,self.hp,self.atk)
#
# aa=Hero(1,1000,200)
#
# aa.sc()
# bb=Hero(2,1222,111)
#
# bb.sc()
#
# print(bb.name)
# print(aa)
class aa():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"{self.name},{self.age}")


Aa = aa(123, 22)
del Aa
