# class Mobil:
#     def __init__(self, merk, warna):
#         self.merk = merk
#         self.warna = warna


# mobil1 = Mobil("Toyota", "Biru")
# mobil2 = Mobil("Avanza", "Hitam")

# print(mobil1.merk)

class Dompet:
    def __init__(self, saldo):
        self.__saldo = saldo

    def saldo_now(self):
        return self.__saldo
    
    def setor(self, jumlah):
        self.__validasi(jumlah)
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        self.__validasi(jumlah)
        if 0 < jumlah < self.__saldo:
            self.__saldo -= jumlah
    def __validasi(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah harus positif")
akun = Dompet(100)
akun.setor(500)
akun.tarik(200)
print(akun.saldo_now())

