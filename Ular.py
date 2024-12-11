from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t\t: ", self.design,
              "\nRacun \t\t\t\t: ", self.racun)
        
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik Solo", "Tidak Berbisa")
anaconda.cetak_ular()

python = Ular("Python", "Ayam", "Hutan", "Bertelur", "Corak Ungu", "Tidak Berbisa")
python.cetak_ular()