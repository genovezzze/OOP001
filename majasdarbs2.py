class Auglis:
    def __init__(self, nosaukums, daudzums):
        self.nosaukums = nosaukums
        self.daudzums = daudzums

class Darzenis:
    def __init__(self, nosaukums, daudzums):
        super().__init__(nosaukums, daudzums)
 

class Puke:
    def __init__(self, nosaukums, daudzums, ziedu_skaits):
        super().__init__(nosaukums, daudzums)