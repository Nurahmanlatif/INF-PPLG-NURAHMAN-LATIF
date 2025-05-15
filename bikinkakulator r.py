def kalkulator():
    """Kalkulator sederhana untuk penjumlahan, pengurangan, perkalian, dan pembagian."""

    try:
        a = float(input("Masukkan angka pertama (oleh Nurahman Latif): "))
        b = float(input("Masukkan angka kedua: "))
        op = input("Pilih operator (+, -, *, /): ")

        if op == '+':
            hasil = a + b
        elif op == '-':
            hasil = a - b
        elif op == '*':
            hasil = a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Tidak bisa membagi dengan nol.")
            hasil = a / b
        else:
            raise ValueError("Operator tidak valid. Gunakan +, -, *, atau /.")

        print("Hasil perhitungan oleh Nurahman Latif adalah:", hasil)

    except ValueError as e:
        print("Terjadi kesalahan input:", e)
    except ZeroDivisionError as e:
        print("Kesalahan matematika:", e)
    except Exception as e:
        print("Terjadi kesalahan yang tidak terduga:", e)

if __name__ == "__main__":
    kalkulator()
