str = "Program Pengambilan Mata Kuliah Peminatan "
x = str.center(50, '=')
print(x)

str = input("Masukkan NIM anda : ")
identitas = str.capitalize()
print("Selamat datang mahasiswa dengan NIM",identitas+ "!")

mata_kuliah = "Mata kuliah peminatan semester ini yaitu Kalkulus,Fisika Dasar,Prokom,Prd,Aeb,dan Material Teknik"
print(mata_kuliah)
peminatan = input("Masukkan mata kuliah peminatan yang akan diambil : ")
pilihan = peminatan.upper()
print("Mata kuliah peminatan yang anda ambil semester ini yaitu",pilihan)


