class programmer:
    company = "MICROSOFT"
    def __init__(self, Name, Product, Salery):
        self.Name = Name
        self.Product = Product
        self.Salery = Salery
    def information(self):
        print(f"The Name of the Programmer is {self.Name}, Work in {self.company} company, his working product is {self.Product} and his Salery is {self.Salery}:  ")

Ahmad = programmer("Ahmad", "Office", input("Enter  your Salery: "))
Ali = programmer("ALi", "edge", input("Enter  your Salery: "))
Aslam = programmer("Aslam", "Skype", input("Enter  your Salery: "))
Ahmad.information()
Ali.information()
Aslam.information()
