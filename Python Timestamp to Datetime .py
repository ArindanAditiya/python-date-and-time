#______
# bagian timestamp ke datetime
#______
# timestamp itu sering dipakai buat nyimpen tanggal + waktu di database
# unix timestamp = jumlah detik dari 1 Januari 1970 UTC
# buat convert timestamp ke datetime, tinggal pakai fromtimestamp()

from datetime import datetime

# ini contoh timestamp (jumlah detik sejak 1970-01-01)
timestamp = 1545730073

# convert timestamp ke object datetime
# fromtimestamp() balikin datetime sesuai timezone lokal komputer
dt_object = datetime.fromtimestamp(timestamp)

# cek hasilnya, sekarang udah jadi object datetime
print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

# catatan:
# kalau mau object datetime-nya dijadiin string dengan format tertentu
# tinggal pakai strftime() kayak yang udah dipelajari sebelumnya

#______
# bagian datetime ke timestamp
#______
# kebalikannya, kalau punya object datetime terus mau dijadikan timestamp
# tinggal pakai method timestamp()

from datetime import datetime

# ambil waktu sekarang dulu, ini object datetime
now = datetime.now()

# convert dari datetime ke timestamp pakai timestamp()
# hasilnya float, isinya detik + microsecond dalam bentuk desimal
ts = datetime.timestamp(now)
print("Timestamp =", ts)

# catatan:
# datetime.fromtimestamp(ts) -> timestamp ke datetime
# datetime.timestamp(dt)     -> datetime ke timestamp
# dua-duanya bolak-balik, jadi bisa dipakai buat simpan/ambil dari database