# ini buat ngubah string jadi object datetime
# namanya strptime() = string parse time
# kebalikannya strftime() yang tadi
from datetime import datetime

# catatan penting:
# nggak semua string bisa dijadikan datetime
# string-nya harus sesuai format tertentu, kalau nggak nanti error

# _________
# bagian string ke object datetime
# _________

date_string = "21 June, 2018"

# cek dulu, ini masih string
print("date_string =", date_string)
print("type of date_string =", type(date_string))

# baru deh diubah ke object datetime pakai strptime()
# argumennya ada 2:
# 1. string yang mau diubah
# 2. format code yang sesuai sama string-nya
date_object = datetime.strptime(date_string, "%d %B, %Y")

# cek hasilnya, sekarang udah jadi object datetime
print("date_object =", date_object)
print("type of date_object =", type(date_object))

# _________
# bagian cara kerja strptime()
# _________
# strptime() itu class method, terima 2 argumen:
# 1. string (yang mau di-convert ke datetime)
# 2. format code (buat kasih tau string-nya formatnya kayak gimana)
# berdasarkan string + format code itu, dia balikin object datetime

# di contoh tadi:
# %d -> day of the month (01, 02, ..., 31)
# %B -> nama bulan lengkap (January, February, ...)
# %Y -> year 4 digit (2018, 2019, ...)

# _________
# bagian contoh string ke datetime (format beda-beda)
# _________

dt_string = "12/11/2018 09:15:32"

# kalau kita anggap tanggalnya format dd/mm/yyyy
# berarti 12 = day, 11 = month, 2018 = year
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)

# kalau kita anggap tanggalnya format mm/dd/yyyy
# berarti 12 = month, 11 = day, 2018 = year
# string sama, tapi hasilnya beda karena format code-nya beda
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)

# _________
# daftar format code yang sering dipakai
# _________
# sebenarnya format code-nya SAMA persis kayak strftime()
# karena strftime() dan strptime() pakai tabel yang sama
# cuma beda arah aja:
# strftime() -> datetime ke string
# strptime() -> string ke datetime

# %a -> nama hari singkat (Sun, Mon, ...)
# %A -> nama hari lengkap (Sunday, Monday, ...)
# %w -> hari sebagai angka (0 = Minggu, 6 = Sabtu)
# %d -> tanggal 2 digit (01, 02, ..., 31)
# %-d -> tanggal tanpa leading zero (1, 2, ..., 30)
# %b -> nama bulan singkat (Jan, Feb, ..., Dec)
# %B -> nama bulan lengkap (January, February, ...)
# %m -> bulan 2 digit (01, 02, ..., 12)
# %-m -> bulan tanpa leading zero (1, 2, ..., 12)
# %y -> year 2 digit (00, 01, ..., 99)
# %-y -> year 2 digit tanpa leading zero (0, 1, ..., 99)
# %Y -> year 4 digit (2013, 2019, etc.)
# %H -> jam 24 jam 2 digit (00, 01, ..., 23)
# %-H -> jam 24 jam tanpa leading zero (0, 1, ..., 23)
# %I -> jam 12 jam 2 digit (01, 02, ..., 12)
# %-I -> jam 12 jam tanpa leading zero (1, 2, ..., 12)
# %p -> AM atau PM
# %M -> menit 2 digit (00, 01, ..., 59)
# %-M -> menit tanpa leading zero (0, 1, ..., 59)
# %S -> detik 2 digit (00, 01, ..., 59)
# %-S -> detik tanpa leading zero (0, 1, ..., 59)
# %f -> microsecond 6 digit (000000 - 999999)
# %z -> UTC offset format +HHMM atau -HHMM
# %Z -> nama timezone
# %j -> hari ke berapa dalam setahun 3 digit (001, 002, ..., 366)
# %-j -> hari ke berapa dalam setahun tanpa leading zero (1, 2, ..., 366)
# %U -> nomor minggu dalam setahun, Minggu dianggap hari pertama (00, 01, ..., 53)
# %W -> nomor minggu dalam setahun, Senin dianggap hari pertama (00, 01, ..., 53)
# %c -> format tanggal + waktu sesuai locale (Mon Sep 30 07:06:05 2013)
# %x -> format tanggal sesuai locale (09/30/13)
# %X -> format waktu sesuai locale (07:06:05)
# %% -> karakter '%' literal

# _________
# bagian ValueError di strptime()
# _________
# kalau string dan format code-nya nggak cocok, bakal kena ValueError

date_string = "12/11/2018"

# ini bakal ERROR karena stringnya pakai '/' (12/11/2018)
# tapi format code-nya pakai spasi (%d %m %Y)
# jadi nggak match
# date_object = datetime.strptime(date_string, "%d %m %Y")
# print("date_object =", date_object)

# hasil error-nya kurang lebih kayak gini:
# ValueError: time data '12/11/2018' does not match format '%d %m %Y'

# yang bener harusnya format code-nya disamain sama stringnya
date_object = datetime.strptime(date_string, "%d/%m/%Y")
print("date_object =", date_object)