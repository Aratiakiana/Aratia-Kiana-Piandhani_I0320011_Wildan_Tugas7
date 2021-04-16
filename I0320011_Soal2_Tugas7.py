print("Program Menghitung Volume dan Diagonal Ruang Sebuah Kolam Berbentuk Balok")
import math
p = float(input('Masukkan panjang kolam : '))
l = float(input('Masukkan lebar kolam : '))
t = float(input('Masukkan tinggi kolam : '))
# Menghitung Volume Kolam
volume = p*l*t
voume_balok = math.ceil(volume)
print("Volume balok yaitu ",math.ceil(volume))
# Menghitung Luas Permukaan Kolam
diagonal_ruang = math.sqrt((p**2)+(l**2)+(t**2))
print("Diagonal ruang kolam yaitu ",math.floor(diagonal_ruang))