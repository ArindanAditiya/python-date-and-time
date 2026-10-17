# ini buat ngubah object datetime jadi string dengan format tertentu
# namanya strftime() = string format time
from datetime import datetime

# ambil waktu sekarang dulu, ini object datetime (belum string)
now = datetime.now()

# %Y -> year 4 digit
year = now.strftime("%Y")
print("year:", year)

# %m -> month 2 digit (01-12)
month = now.strftime("%m")
print("month:", month)

# %d -> day 2 digit (01-31)
day = now.strftime("%d")
print("day:", day)

# %H:%M:%S -> jam:menit:detik (24 jam)
time = now.strftime("%H:%M:%S")
print("time:", time)

# format bebas, bisa gabungin banyak format code sekaligus
# ini gaya US: mm/dd/YYYY, H:M:S
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)

# bagian cara kerja strftime()
# %Y, %m, %d, dll itu namanya format code
# strftime() terima satu atau lebih format code, terus balikin string
# yang di atas tadi year, day, time, date_time semuanya STRING
# sedangkan now itu masih OBJECT datetime

# bagian bikin string dari timestamp

# ini kebalikan dari sebelumnya, dari unix timestamp dijadikan object datetime
timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)
print("Date time object:", date_time)  # masih object datetime

# baru deh diubah ke string pakai strftime()
# format mm/dd/YYYY, H:M:S
d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)

# %d = day, %b = nama bulan singkat (Jun), %Y = year
d = date_time.strftime("%d %b, %Y")
print("Output 3:", d)

# %d = day, %B = nama bulan lengkap (June), %Y = year
d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)

# %I = jam format 12 jam, %p = AM/PM
d = date_time.strftime("%I%p")
print("Output 5:", d)

# daftar format code yang sering dipakai
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

# bagian format sesuai locale
# %c, %x, %X itu format yang ngikutin setting locale komputer
# jadi hasilnya bisa beda-beda tergantung locale-nya

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

# %c -> tanggal + waktu lengkap versi locale
d = date_time.strftime("%c")
print("Output 1:", d)

# %x -> tanggal aja versi locale
d = date_time.strftime("%x")
print("Output 2:", d)

# %X -> waktu aja versi locale
d = date_time.strftime("%X")
print("Output 3:", d)

# catatan: strptime() itu kebalikannya strftime()
# strftime() -> object datetime jadi string
# strptime() -> string jadi object datetime