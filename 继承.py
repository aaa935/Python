# class Master():
#     def __init__(self):
#         self.kongfu = "古法煎饼果子配方"
#
#     def make_cake(self):
#         print(f"使用{self.kongfu}制作了一套煎饼果子")
#
#
# class School():
#     def __init__(self):
#         self.kongfu = "现代煎饼果子配方"
#
#     def make_cake(self):
#         print(f"使用{self.kongfu}制作了一套煎饼果子")
#
#
# class TuDi(Master, School):
#     def __init__(self):
#         Master.__init__(self)
#         self.kongfu_master = self.kongfu
#         School.__init__(self)
#         self.kongfu_school = self.kongfu
#
#     def make_cake_master(self):
#         self.kongfu = self.kongfu_master
#         Master.make_cake(self)
#
#     def make_cake_school(self):
#         self.kongfu = self.kongfu_school
#         School.make_cake(self)
#
#
# DaMao = TuDi()
# print(TuDi.__mro__)
# DaMao.make_cake_master()
# DaMao.make_cake_school()
# class Master():
#     def __init__(self):
#         self.kongfu = "古法"
#
#     def cook_cake(self):
#         return self.kongfu
#
#
# class School():
#     def __init__(self):
#         self.kongfu = "现代"
#
#     def cook_cake(self):
#         return self.kongfu
#
#
# class TuDi(Master, School):
#     def __init__(self):
#         Master.__init__(self)
#         self.kongfu_Master = self.kongfu
#         School.__init__(self)
#         self.kongfu_School = self.kongfu
#
#     def cook_cake_Master(self):
#         self.kongfu=self.kongfu_Master
#         print(self.cook_cake())
#
#     def cook_cake_School(self):
#         self.kongfu=self.kongfu_School
#         print(self.cook_cake())
#
#
# DaMao = TuDi()
# DaMao.cook_cake_Master()
# DaMao.cook_cake_School()

#
# class Master():
#     def __init__(self):
#         self.kongfu = "古法"
#
#     def cook_cake(self):
#         return self.kongfu
#
#
# class School():
#     def __init__(self):
#         self.kongfu = "现代"
#
#     def cook_cake(self):
#         return self.kongfu
#
#
# class TuDi(Master, School):
#     def __init__(self):
#         Master.__init__(self)
#         self.cook_cake_Master = self.kongfu
#         School.__init__(self)
#         self.cook_cake_School = self.kongfu
#
#     def make_cook_cake_Master(self):
#
#         return self.cook_cake_Master
#
#     def make_cook_cake_School(self):
#
#         return self.cook_cake_School
#
# DaMao = TuDi()
# print(DaMao.make_cook_cake_School())
# print(DaMao.make_cook_cake_Master())

# class Master():
#     def __init__(self):
#         self.kongfu = "古法"
#
#     def cook_cake(self):
#         return self.kongfu
#
#
# class School():
#     def __init__(self):
#         self.kongfu = "现代"
#
#     def cook_cake(self):
#         return self.kongfu
#
#
# class TuDi(Master, School):
#     def __init__(self):
#         Master.__init__(self)
#         self.cook_cake_Master = self.kongfu
#         School.__init__(self)
#         self.cook_cake_School = self.kongfu
#
#     def make_cook_cake_Master(self):
#         print(self.cook_cake_Master)
#
#     def make_cook_cake_School(self):
#         print(self.cook_cake_School)
#
#
# DaMao = TuDi()
# DaMao.make_cook_cake_School()
# DaMao.make_cook_cake_Master()
# class Master():
#     def __init__(self):
#         self.kongfu = "古法"
#
#     def cook_cake(self):
#         return self.kongfu
#
#
# class School():
#     def __init__(self):
#         self.kongfu = "现代"
#
#     def cook_cake(self):
#         return self.kongfu
#
#
# class DaMao(Master, School):
#     def __init__(self):
#         self.kongfu = "猫式"
#         self.cook_cake_Mao = self.kongfu
#         Master.__init__(self)
#         self.cook_cake_Master = self.kongfu
#         School.__init__(self)
#         self.cook_cake_School = self.kongfu
#
#     def make_cook_cake_Mao(self):
#         print(self.cook_cake_Mao)
#
#     def make_cook_cake_Master(self):
#         print(self.cook_cake_Master)
#
#     def make_cook_cake_School(self):
#         print(self.cook_cake_School)
#
#
# class TuSun(DaMao):
#     def __init__(self):
#         super().__init__()
#         self.kongfu = "徒孙"
#         self.cook_cake_TS = self.kongfu
#
#     def make_cake_ts(self):
#         print(self.cook_cake_TS)
#
#
# damao = DaMao()
# print(DaMao.__mro__)
# damao.make_cook_cake_Mao()
# damao.make_cook_cake_Master()
# damao.make_cook_cake_School()
# print(TuSun.__mro__)
# ts = TuSun()

class Master():
    def __init__(self):
        self.kongfu = "古法"

    def cook_cake(self):
        return self.kongfu


class School():
    def __init__(self):
        self.kongfu = "现代"

    def cook_cake(self):
        return self.kongfu


class DaMao(Master, School):
    def __init__(self):
        self.kongfu = "猫式"
        self.cook_cake_Mao = self.kongfu
        Master.__init__(self)
        self.cook_cake_Master = self.kongfu
        School.__init__(self)
        self.cook_cake_School = self.kongfu

    def make_cook_cake_Mao(self):
        print(self.cook_cake_Mao)

    def make_cook_cake_Master(self):
        print(self.cook_cake_Master)

    def make_cook_cake_School(self):
        print(self.cook_cake_School)


class TuSun(DaMao):
    def __init__(self):
        super().__init__()
        self.kongfu = "徒孙"
        self.cook_cake_TS = self.kongfu

    def make_cake_ts(self):
        print(self.cook_cake_TS)


damao = DaMao()
print(DaMao.__mro__)
damao.make_cook_cake_Mao()
damao.make_cook_cake_Master()
damao.make_cook_cake_School()
print(TuSun.__mro__)
ts = TuSun()

ts.make_cook_cake_Mao()
ts.make_cook_cake_School()
ts.make_cook_cake_Master()
ts.make_cake_ts()
