# __________
# bagian time.ctime()
# __________
# ctime() itu nerima detik sejak epoch (unix timestamp)
# terus balikin string waktu lokal yang udah kebaca manusia

import time

# detik sejak epoch (dari 1 Januari 1970)
seconds = 1672215379.5045543

# convert detik tadi ke format yang kebaca
local_time = time.ctime(seconds)
print("Local time:", local_time)

# __________
# bagian time.sleep()
# __________
# sleep() itu buat nge-pause / nunda eksekusi program
# seberapa lama? sesuai jumlah detik yang dioper

print("Printed immediately.")
time.sleep(2.4)  # program berhenti dulu 2.4 detik di sini
print("Printed after 2.4 seconds.")

# urutannya:
# 1. "Printed immediately" langsung ke-print
# 2. time.sleep(2.4) -> program nunggu 2.4 detik
# 3. baru deh "Printed after 2.4 seconds" ke-print

# __________
# bagian time.localtime()
# __________
# localtime() nerima detik sejak epoch
# terus balikin struct_time dalam waktu LOKAL
# struct_time itu tuple isi 9 elemen

result = time.localtime(1672214933)
print("result:", result)

# kita bisa akses elemen-elemennya pakai nama attribute
print("\nyear:", result.tm_year)      # tahun
print("tm_hour:", result.tm_hour)     # jam

# catatan:
# kalau localtime() dipanggil tanpa argumen / None
# dia otomatis pakai waktu sekarang (hasil dari time())

# __________
# bagian time.gmtime()
# __________
# gmtime() hampir sama kayak localtime()
# bedanya: gmtime() balikin waktu dalam UTC (bukan lokal)

result = time.gmtime(1672214933)
print("result:", result)

# akses elemen-elemennya sama kayak localtime()
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

# catatan:
# sama kayak localtime(), kalau tanpa argumen / None
# bakal pakai waktu sekarang

# __________
# bagian time.mktime()
# __________
# mktime() itu kebalikannya localtime()
# dia nerima struct_time (tuple 9 elemen) -> balikin detik sejak epoch (lokal)

# struktur struct_time:
# (year, month, day, hour, minute, second, weekday, day of the year, daylight saving)

time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

# convert time_tuple ke detik sejak epoch
seconds = time.mktime(time_tuple)
print(seconds)

# __________
# bagian time.asctime()
# __________
# asctime() nerima struct_time (atau tuple yang strukturnya sama)
# terus balikin string waktu yang kebaca manusia

# strukturnya sama kayak mktime() tadi:
# (year, month, day, hour, minute, second, weekday, day of the year, daylight saving)

t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)

# hasilnya: string waktu lengkap dalam format yang gampang dibaca

# __________
# bagian time.strftime()
# __________
# strftime() di module time itu mirip kayak di datetime
# bedanya: di sini dia butuh 2 argumen:
# 1. format code
# 2. struct_time (atau tuple yang strukturnya sama)

named_tuple = time.localtime()  # ambil struct_time waktu sekarang

# format hasilnya sesuai format code yang dipakai
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print(time_string)

# format code yang umum dipakai:
# %Y - year [0001, ..., 2018, 2019, ..., 9999]
# %m - month [01, 02, ..., 11, 12]
# %d - day [01, 02, ..., 30, 31]
# %H - hour [00, 01, ..., 22, 23]
# %M - minutes [00, 01, ..., 58, 59]
# %S - second [00, 01, ..., 58, 61]

# __________
# bagian time.strptime()
# __________
# strptime() itu kebalikannya strftime()
# dia parse string jadi struct_time
# argumennya: string + format code

time_string = "14 July, 2023"

# parse string jadi struct_time
# %d = day, %B = nama bulan lengkap, %Y = year 4 digit
result = time.strptime(time_string, "%d %B, %Y")
print(result)

# hasilnya struct_time, mirip kayak localtime() cuma ini dari string

# __________
# ringkasan singkat
# __________
# ctime(seconds)        -> detik ke string lokal
# sleep(seconds)        -> pause program
# localtime([seconds])  -> detik ke struct_time lokal
# gmtime([seconds])     -> detik ke struct_time UTC
# mktime(struct_time)   -> struct_time ke detik (lokal)
# asctime(struct_time)  -> struct_time ke string
# strftime(fmt, struct) -> struct_time ke string dengan format custom
# strptime(str, fmt)    -> string ke struct_time