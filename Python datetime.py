# ini adalah untuk mengambil waktu yang paling lengkap
import datetime
from datetime import date, time, timedelta
import pytz

#timepastamp sekarang
now  = datetime.datetime.now()
print(now)

# ini contoh digunakan kalau mau mengambil tanggal pada hari ini
current_date = datetime.date.today()
print(current_date)

# kita bisa pakai fungsi dir() untuk ambil daftar
print(dir(datetime))

# bagian datetime.date class

# ini cara bikin object date manual, isinya (year, month, day)
d = datetime.date(2022, 12, 25)
print(d)

# bisa juga langsung pakai class date-nya aja biar ga nulis datetime.date terus
d = date(2022, 12, 25)
print(d)

# ini buat ambil tanggal hari ini pakai today()
todays_date = date.today()
print("Today's date =", todays_date)

# ini buat convert dari unix timestamp ke date
# timestamp itu jumlah detik dari 1 Januari 1970 UTC
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

# kita bisa ambil year, month, day dari object date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# bagian datetime.time class

# ini buat bikin object time, formatnya (hour, minute, second, microsecond)
# time(hour = 0, minute = 0, second = 0) -> default semua 0
a = time()
print(a)

# time(hour, minute and second)
b = time(11, 34, 56)
print(b)

# ini juga sama aja, cuma pakai keyword argument
c = time(hour = 11, minute = 34, second = 56)
print(c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print(d)

# ini cara ambil attribute dari object time
a = time(11, 34, 56)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Second =", a.second)
print("Microsecond =", a.microsecond)  # default 0 kalau ga diisi

# bagian datetime.datetime class
# ini gabungan date + time, paling lengkap

# datetime(year, month, day) -> jam otomatis 00:00:00
a = datetime.datetime(2022, 12, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime.datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)

# ini cara ambil attribute-attribute dari object datetime
a = datetime.datetime(2022, 12, 28, 23, 55, 59, 342380)
print("Year =", a.year)
print("Month =", a.month)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Timestamp =", a.timestamp())  # convert ke unix timestamp

# bagian datetime.timedelta class
# ini buat selisih antara dua tanggal/waktu

# contoh pakai date() -> hasilnya selisih hari
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

# contoh pakai datetime() -> hasilnya lebih detail (hari, jam, menit, detik)
t4 = datetime.datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime.datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

# cek tipe datanya, ternyata hasil pengurangan date/datetime itu timedelta
print("Type of t3 =", type(t3))
print("Type of t6 =", type(t6))

# ini cara bikin timedelta manual, terus dihitung selisihnya
t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("t3 =", t3)

# bisa juga convert timedelta ke total detik pakai total_seconds()
t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("Total seconds =", t.total_seconds())

# bagian format datetime
# beda negara beda format tanggal, US pakai mm/dd/yyyy, UK pakai dd/mm/yyyy
# makanya kita butuh strftime() sama strptime()

# strftime() -> object datetime diubah jadi string dengan format tertentu
now = datetime.datetime.now()

# format jam:menit:detik
t = now.strftime("%H:%M:%S")
print("Time:", t)

# format mm/dd/YYYY, H:M:S (gaya US)
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("s1:", s1)

# format dd/mm/YYYY, H:M:S (gaya UK)
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("s2:", s2)

# format code yang umum dipakai:
# %Y - year
# %m - month
# %d - day
# %H - hour
# %M - minute
# %S - second

# strptime() -> kebalikannya, dari string diubah jadi object datetime
date_string = "25 December, 2022"
print("date_string =", date_string)

# %d = day, %B = nama bulan lengkap, %Y = year
date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# bagian handling timezone
# buat urusan timezone mending pakai library pytz aja, jangan bikin sendiri

# waktu lokal
local = datetime.datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

# waktu New York
tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

# waktu London
tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))