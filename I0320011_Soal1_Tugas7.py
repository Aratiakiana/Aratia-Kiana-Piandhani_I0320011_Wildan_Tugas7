str = "Program Pemilihan Mata Kuliah Peminatan "
x = str.center(50, '=')
print(x)

str = input("Masukkan NIM anda : ")
identitas = str.capitalize()
print("Selamat datang mahasiswa dengan NIM",identitas+ "!")

mata_kuliah = "Mata kuliah peminatan semester ini yaitu Kalkulus,Fisika Dasar,Prokom,Prd,Aeb,dan Material Teknik"
print(mata_kuliah)
peminatan = input("Masukkan mata kuliah peminatan yang akan dipilih : ")
pilihan = peminatan.upper()
print("Mata kuliah peminatan yang anda pilih semester ini yaitu",pilihan)


