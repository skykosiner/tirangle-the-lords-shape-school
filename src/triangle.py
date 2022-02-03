class Triangle:
    def input(self):
        self.a = float(input("Enter the length of the first side: "))
        self.b = float(input("Enter the length of the second side: "))
        self.c = float(input("Enter the length of the third side: "))

    def check(self):
        if self.a == self.b and self.b != self.c and self.a != self.c:
            print("This is an isosceles triangle nice")
        elif self.b == self.c and self.b != self.a and self.a != self.c:
            print("Hmm an isosceles triangle")
        elif self.c == self.a and self.a != self.b and self.c != self.b:
            print("You good sir have an isosceles triangle")
        else:
            print("There was an error, that aint an isosceles triangle")
