#Python
#Nama    : Nur Ahmad Wibisono
#NRP     : 5007221007
#Jurusan : Teknik Mesin

#kecepatan tangensial tidak boleh lebih dari 30
#sudut tembakan 45 derajat
#gravitasi 10
import math

input = 30

if(1 <= input <= 10) : losses = 1
if(11 <= input <= 20) : losses = 3
if(21 <= input <= 30) : losses = 5

#Menghitung Jarak Maksimal

x = input - losses

#menggunakan rumus : jarak = x^2 dikali sin  2*45 / g
#g = 10
#sin 90 = 1

jarak = int(x**2 * 1 / 10)

#Mencari Kecepatan Tangensial

kecepatantangensial = float(math.sqrt(jarak * 10 / 1)) + losses

print("jarak = ", jarak, "kecepatan = ", kecepatantangensial)








