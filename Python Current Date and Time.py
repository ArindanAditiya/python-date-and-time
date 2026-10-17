# ini buat ngambil tanggal hari ini pakai class date
# date.today() -> balikin object date (tanggal lokal sekarang)
from datetime import date

today = date.today()
print("Today's date:", today)

# __________
# bagian current date dalam berbagai format
# __________
# tanggal yang sama bisa ditampilin dengan format yang beda-beda
# tinggal mainin format code di strftime()

today = date.today()

# format dd/mm/YYYY -> gaya UK/Indonesia
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# format nama bulan lengkap, day, year
# %B = nama bulan lengkap (December), %d = day, %Y = year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# format mm/dd/yy -> gaya US, year cuma 2 digit
# %m = month, %d = day, %y = year 2 digit
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# format nama bulan singkat, day, year pakai strip
# %b = nama bulan singkat (Dec)
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

# __________
# bagian ngambil tanggal + waktu sekarang
# __________
# kalau butuh tanggal SEKALIGUS jam, pakai class datetime
# bukan date doang

from datetime import datetime

# datetime.now() -> balikin object datetime berisi tanggal + waktu lokal sekarang
now = datetime.now()
print("now =", now)

# object datetime tadi diubah ke string pakai strftime()
# format dd/mm/YYYY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# catatan:
# date.today() -> cuma tanggal (year, month, day)
# datetime.now() -> tanggal + waktu lengkap (year, month, day, hour, minute, second, microsecond)