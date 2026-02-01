class Lingkaran:
    def __init__(self, radius):
        self._radius = radius

    @property # Getter
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):  #Setter
        if value <= 0:
            raise ValueError("Radius harus positif")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Menghapus Radius....")
        del self._radius

    @property
    def area(self):
        return 3.14 * (self._radius**2)
    
lingkar = Lingkaran(3)
print(f"Radius Awal: {lingkar.radius}")

lingkar.radius = 8
print(f"Setelah mengubah radius: {lingkar.radius}")

print(lingkar.area)

del lingkar.radius
print("Radius dihapus!")

try:
    lingkar.radius
except AttributeError as e:
    print("Error", e)