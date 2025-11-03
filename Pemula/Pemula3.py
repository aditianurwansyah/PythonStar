print("==============================================================")
print("||        Selamat datang di program belajar Python Lanjutan!       ||")
print("==============================================================")
print("Halo user!")
print("Hari ini kita akan belajar tentang konsep lanjutan dalam Python.")
print("Kita akan mulai dengan memahami fungsi dan modul.")
def sapa_user(nama):
    print(f"Halo! {nama}, selamat datang kembali di program belajar Python lanjutan.")
nama = input("Siapa nama kamu? ")
sapa_user(nama)
print("Sekarang, mari kita coba membuat fungsi sederhana untuk menghitung faktorial sebuah angka.")
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
angka = int(input("Masukkan angka untuk menghitung faktorialnya: "))
hasil = faktorial(angka)
print(f"Hasil faktorial dari {angka} adalah {hasil}")
print("Terima kasih telah belajar Python lanjutan bersama kami hari ini!")
print("Sampai jumpa lagi!") 
