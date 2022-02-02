class Triangle:
    def input(self):
        self.a = float(input("Enter the length of the first side: "))
        self.b = float(input("Enter the length of the second side: "))
        self.c = float(input("Enter the length of the third side: "))

    def check(self):
        if self.a == self.b or self.b == self.c or self.a == self.c:
            print("The triangle is valid yaya")
        else:
            print("This aint it chief")
            exit(0x45)
