# ==========================================
# bagian ngambil jam sekarang pakai datetime object
# ==========================================
# ini cara paling umum, pakai class datetime
# nanti tinggal di-strftime() buat ambil jam-nya aja

from datetime import datetime

# datetime.now() -> object datetime isi tanggal + waktu sekarang
now = datetime.now()

# ambil jam:menit:detik aja pakai strftime()
# %H = jam 24 jam, %M = menit, %S = detik
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# ==========================================
# bagian ngambil jam sekarang pakai module time
# ==========================================
# selain datetime, ada juga module time
# bedanya: time module lebih sederhana, fokusnya ke waktu

import time

# time.localtime() -> balikin struct_time isi waktu lokal sekarang
t = time.localtime()

# time.strftime() di sini butuh 2 argumen:
# 1. format code
# 2. struct_time (hasil dari localtime tadi)
# beda sama datetime.strftime() yang cuma butuh format code
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

# ==========================================
# bagian ngambil jam di timezone tertentu
# ==========================================
# kalau butuh jam di timezone lain, pakai library pytz
# tinggal oper timezone object ke datetime.now()

from datetime import datetime
import pytz

# bikin timezone object buat New York dulu
tz_NY = pytz.timezone('America/New_York')

# masukin timezone object tadi ke datetime.now()
# jadi sekarang datetime-nya ngikutin waktu New York
datetime_NY = datetime.now(tz_NY)

# format jadi jam:menit:detik terus print
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

# sama kayak tadi, tapi buat London
tz_London = pytz.timezone('Europe/London')

# ambil waktu London sekarang
datetime_London = datetime.now(tz_London)

# format terus print
print("London time:", datetime_London.strftime("%H:%M:%S"))

# catatan:
# datetime.now() tanpa argumen -> waktu lokal komputer
# datetime.now(tz) -> waktu sesuai timezone yang dioper
# time module lebih simpel tapi fiturnya lebih terbatas
# pytz itu library pihak ketiga, jadi harus install dulu: pip install pytz