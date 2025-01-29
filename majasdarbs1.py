class Turnirs:
    def __init__(self, nosaukums, cilvekuskaits, komanduskaits, sportaveids):
        self.nosaukums = nosaukums
        self.cilvekuskaits = cilvekuskaits
        self.komanduskaits = komanduskaits
        self.sportaveids = sportaveids
        self.sponsorusaraksts = []
    def sponsors(self, sponsors):
        self.sponsorusaraksts.append(sponsors)
    def izvade(self):
        sponsors = "\n".join(self.sponsorusaraksts)
        return (f"Šis ir {self.sportaveids} turnīrs “{self.nosaukums}”, kurā piedalās {self.cilvekuskaits} cilvēki, "
                f"{self.komanduskaits} komandas.\nSponsori:\n{sponsors}")

turnirs1 = Turnirs("World Cup", 720, 36, "Futbols")
turnirs1.sponsors("Adidas")
turnirs1.sponsors("Nike")
turnirs1.sponsors("BMW")

turnirs2 = Turnirs("Bespalova Cup", 32, 8, "Volejbols")
turnirs2.sponsors("Rimi")
turnirs2.sponsors("Maxima")
turnirs2.sponsors("Citro")

turnirs1.izvade()
turnirs2.izvade()