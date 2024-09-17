print("Hello!")
class Cilveks: 
    def __init__(self, name, sex, age = 0):
        self.vards = name
        self.vecums = age
        self.dzimums = sex
    
    def pastastit_par_sevi(self):

        if self.dzimums == "s":
            teksts = "sieviete"
        elif self.dzimums == "v":
            teksts = "virietis"
        else:
            teksts = self.dzimums
        print("Sveiki, mani sauc {}, esmu {}, man ir {} gadi.".format(self.vards, teksts, self.vecums))
        return "Sveiki, mani sauc {}, esmu {}, man ir {} gadi.".format(self.vards, teksts, self.vecums)

    def svinet_dz_d(self):
        self.vecums += 1
        self.info()
    
    def mainit_vardu(self, jaunais_vards):
        self.vards = jaunais_vards
        self.info()
    
    def mainit_dzimumu(self, jaunais_dzimums = ""):
        if jaunais_dzimums == "":
            if self.dzimums == "s":
                self.dzimums = "v"
            else:
                self.dzimums = "s"
        else:
            self.dzimums = jaunais_dzimums
        self.info()

class Sieviete(Cilveks):
    def __init__(self, name, hair_color, age = 0):
        super().__init__(name, "s", age)
        self.matu_krasa = hair_color 
        self.info()    

    def info(self):
        super().info()
        print("Mana matu krāsa ir", self.matu_krasa)  

# persona 1 =Cilveks("Anna", 18, "s")
# persona.pastastit_par_sevi()

# persona 2 = Sieviete("Karlina", "blonda", "s", 20)
