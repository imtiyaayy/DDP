from gempa import *

gempaPertama = Gempa(1.2, 'Banten')
gempaPertama.dampak()
print(f'Jumlah Gempa {Gempa.jumlahGempa}')
gempaKedua = Gempa(6.1, 'Palu')
gempaKedua.dampak()
print(f'Jumlah Gempa {Gempa.jumlahGempa}')
gempaKetiga = Gempa(5.6, 'Cianjur')
gempaKetiga.dampak()
print(f'Jumlah Gempa {Gempa.jumlahGempa}')
gempaKeempat = Gempa(3.3, 'Jayapura')
gempaKeempat.dampak()
print(f'Jumlah Gempa {Gempa.jumlahGempa}')
gempaKelima = Gempa(4.0, 'Banten')
gempaKelima.dampak()
print(f'Jumlah Gempa {Gempa.jumlahGempa}')