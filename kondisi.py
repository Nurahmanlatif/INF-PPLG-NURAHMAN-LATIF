# Program untuk menentukan kondisi berdasarkan suhu
suhu=int(input("masukan suhu : "))

if suhu >= 35:
    print("Hari ini sangat panas! Jangan lupa minum air putih.")
elif suhu >= 25:
    print("Cuaca cukup hangat dan menyenangkan.")
elif suhu >= 15:
    print("Cuaca agak dingin, sebaiknya pakai jaket.")
elif suhu >= 5:
    print("Cuaca dingin, kenakan pakaian hangat.")
else:
    print("Suhu ekstrem! Tetap di dalam rumah jika memungkinkan.")
