class Gempa:
    # lokasi = ""
    # skala = 0

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def data_gempa(self):
        if (self.skala < 2):
            ket = "Gempa tidak berasa"
        elif (self.skala >= 2 and self.skala < 4):
            ket = "Dampak gempa bangunan retak-retak"
        elif (self.skala >=4 and self.skala <6):
            ket = "Dampak gempa bangunan roboh"
        elif (self.skala > 6):
            ket = "Dampaj gempa bangunan roboh dan berpotensi tsunami"
        else:
            ket = "alhamdulilah aman"

        print(f"Gempa di{self.lokasi} dengan skala {self.skala} : {ket}") 