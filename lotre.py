import random

def pick_unique_numbers(digit_count):
    if 1 <= digit_count <= 5:
        return random.sample(range(1, 81), digit_count)
    else:
        raise ValueError("digit_count harus antara 1 sampai 5")

# Interaktif: user pilih berapa digit
try:
    jumlah_digit = int(input("Mau ambil berapa digit (1-5)? "))
    hasil = pick_unique_numbers(jumlah_digit)
    print(f"Hasil ({jumlah_digit} digit): {', '.join(map(str, hasil))}")
except ValueError as e:
    print("Input tidak valid. Masukkan angka antara 1 sampai 5.")
