from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, suara):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.suara = suara

    def cetak_burung(self):
        super().cetak()
        print("Paruh \t\t\t\t: ", self.paruh,
              "\nSuara \t\t\t\t: ", self.suara)
        
pelikan = Burung("Pelikan", "Ikan", "Air", "Beranak", "Panjang dan memiliki kantong besar", "berderum atau berdengung")
pelikan.cetak_burung()

kakatua = Burung("Kaka Tua", "Sayur-sayuran", "Udara", "Bertelur", "Kuat dan melengkung", "Nyaring, beragam dan ekspresif")
kakatua.cetak_burung()