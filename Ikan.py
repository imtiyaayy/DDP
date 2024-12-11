from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, suara):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.suara = suara

    def cetak_ikan(self):
        super().cetak()
        print("Design \t\t\t\t: ", self.design,
              "\nSuara \t\t\t\t: ", self.suara)
        
lumbalumba = Ikan("Lumba-lumba", "Udang", "Sungai Mahakam", "Melahirkan", "halus licin tidak bersisik", "Siulan yang khas")
lumbalumba.cetak_ikan()

nemo = Ikan("Nemo", "Plankton dan Alga", "Laut dan Terumbu karang", "Bertelur", "berwarna oranye cerah dan tiga garis putih dibadannya", "blubuk blubuk")
nemo.cetak_ikan()