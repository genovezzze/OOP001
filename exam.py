class Doktorats:
    def __init__(self, nosaukums, pacientuSkaits):
        self.nosaukums=nosaukums
        self.pacientuSkaits=pacientuSkaits
    def ievade(self):
        self.nosaukums = input("Ievadi nosaukumu --> ")
        try:
            self.pacientuSkaits=int(input("Ievadi pacientu skaits --> "))
        except:
            self.pacientuSkaits=0
        finally:
            print("Ievade veiksmīga", self.pacientuSkaits)


            def izvade(self):
                print(f"Doktorāts {self.nosaukums} apkalpo {self.pacientuSkaits} pacientus.")

d1 = Doktorats("Zemlejas", -325)
d1.ievade()
d1.ievade()
d1.ievade()
d2 = Doktorats("Kaka", 340)
d2.ievade()
d2.ievade()
d2.ievade()
print(d2)

    