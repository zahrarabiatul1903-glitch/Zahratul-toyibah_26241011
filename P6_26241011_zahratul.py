Nama = "Zahratul Toyibah"
Nim = "26241011"
A = 1
B = 1

print("Nama : ", Nama)
print("Nim : ", Nim)

a = int(input("Digit A: "))
b = int(input("Digit B: "))

Kondisi1 = a >= 5
Kondisi2 = b >= 5

print("Kondisi 1 >= 5 :", Kondisi1)
print("Kondisi 2 >= 5 :", Kondisi2)

print("NOT:", not Kondisi1)
print("AND:", Kondisi1 and Kondisi2)
print("OR:", Kondisi1 or Kondisi2)
print("XOR:", Kondisi1 ^ Kondisi2)

#Penjelasan OR dan XOR:
#OR :true apabila salah satu kondisi benar
#XOR :true apabila kedua kondisi memiliki hasil yang berbeda