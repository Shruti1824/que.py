class Mydate:
    def accept(self):
        self.d=int(input("Enter day"))
        self.m=int(input("Enter month"))
        self.y=int(input("Enter year "))

        def display(self):
            try:
                if self.d>31:
                    raise
                ValueError("month value is greater than 12")
                print("Date is:",self.d,"-",self.m,"-",self.y)
            except ValueError as e:
                obj=Mydate()
                obj.accept()
                obj.display()