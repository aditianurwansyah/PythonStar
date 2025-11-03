print("==========================================================")
print("Selamat datang di program Python sederhana!")
print("==========================================================")
print("hari ini kita akan belajar tentang perulangan dan pengkondisian.")
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
print("==========================================================")
if umur < 0:
    print("Umur tidak boleh negatif!")
elif umur < 18:
    print(f"Halo, {nama}! Anda masih di bawah umur.")
else:
    print(f"Halo, {nama}! Anda sudah dewasa.")
print("Terima kasih telah menggunakan program ini.")
print("==========================================================")
print("Program selesai. Sampai jumpa lagi!")
print("==========================================================")

print("Sekarang, mari kita coba perulangan.")
for i in range(1, 6):
    print(f"Perulangan ke-{i}")
print("Perulangan selesai.")
print("==========================================================")
print("Terima kasih telah belajar bersama kami!")
