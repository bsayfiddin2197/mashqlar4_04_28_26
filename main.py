class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def info(self):
        print(f"Ismi: {self.ism}")
        print(f"Maosh: {self.maosh}")

class Dasturchi(Xodim):
    def __init__(self, ism, maosh, til):
        super().__init__(ism, maosh)
        self.til = til
    def info(self):
        super().info()
        print(f"Til: {self.til}")

x = Dasturchi("Aziz", 500, "Python")
x.info()
