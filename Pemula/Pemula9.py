print("-=========================================================")
print("Selamat datang di program Python sederhana!")
print("disini akan belajar tentang switch case menggunakan dictionary")
print("-=========================================================")
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
print("-=========================================================")
print(f"Halo, {nama}! Anda berumur {umur} tahun.")
# Menggunakan dictionary untuk mensimulasikan switch case
def switch_case(umur):
    switcher = {
        0: "Anda baru saja lahir!",
        1: "Anda adalah bayi.",
        2: "Anda adalah balita.",
        3: "Anda adalah anak-anak.",
        4: "Anda adalah pra-remaja.",
        5: "Anda adalah remaja.",
    }
    return switcher.get(umur, "Anda sudah dewasa.")
print(switch_case(umur))
print("Terima kasih telah menggunakan program ini.")
print("-=========================================================")
print("Program selesai. Sampai jumpa lagi!")
print("-=========================================================") 