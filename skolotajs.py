class Skolotajs:

    stunduSkNedela=0

    skolotajaTips=0

    uzvards="Nezinams"

    klase="x.i"

class SakumskolasSkolotajs(Skolotajs):

    def init(self):

        self.skolotajaTips=1

    def izvade(self):

        print(f"Sākumskolas (tips - {self.skolotajaTips}) skolotājs Bērziņš māca 15 stundas 2.a klasē.")

class VidusskolasSkolotajs(Skolotajs):

    def init(self):

        self.skolotajaTips=3

        self.uzvards="Ozols"

    pirmaisPrieksmets="Matemātika"

    otraisPrieksmets="Datorika"

    pirmaisPrieksmetsStundas=12

    otraisPrieksmetsStundas=8

    def cikStundasKopa(self):

        self.StunduSkaitsNedela=self.pirmaisPrieksmetsStundas+self.otraisPrieksmetsStundas

        return self.StunduSkaitsNedela

    def izvade(self):

        print(f"Vidusskolas (tips - {self.skolotajaTips}) skolotājs Ozols māca šādus priekšmetus: matemātika un datorika, kopā 20 stundas.")

ss1=SakumskolasSkolotajs()

#ss1.ievade()

ss1.izvade()

vsk2=VidusskolasSkolotajs()

vsk2.izvade()