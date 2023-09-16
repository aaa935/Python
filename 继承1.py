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
        self.kongfu_Mao=self.kongfu

    def cook_cake(self):
        print(self.kongfu_Mao)


    def make_cook_cake_Master(self):
        Master.__init__(self)

        # print(self.kongfu)
        print(Master.cook_cake(self))
    def make_cook_cake_School(self):
        School.__init__(self)

        # print(self.kongfu)
        print(School.cook_cake(self))

damao = DaMao()
print(DaMao.__mro__)

damao.make_cook_cake_Master()
damao.make_cook_cake_School()
damao.cook_cake()
