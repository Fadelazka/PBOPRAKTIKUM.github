Penjelasan untuk Panduan Kamu
Agar kamu paham dan bisa menjelaskan saat asistensi, berikut poin-poin pentingnya:

OOP & Widget Dasar:

Kita menggunakan tk.Tk() sebagai jendela utama (Object).

tk.Frame digunakan sebagai wadah (container) agar elemen di dalamnya bisa dikelompokkan. Di sini saya menggunakannya untuk membuat efek "Card" (kotak putih di tengah).

entry_user.get() adalah cara kita mengambil teks yang diketik user.

Validasi (Tugas Mandiri A):

Pada fungsi login dan register, saya menambahkan if user == "" or pwd == "".

Perintah strip() digunakan untuk menghapus spasi di awal/akhir supaya user tidak bisa "mengakali" dengan hanya mengetik spasi.

Jika kosong, messagebox.showwarning akan muncul dan fungsi dihentikan dengan perintah return.

Halaman Lanjutan (Tugas Mandiri B):

tk.Toplevel(root) digunakan untuk membuat jendela baru yang muncul di atas jendela utama.

Fungsi buka_halaman_utama dipanggil hanya jika username dan password cocok dengan data di file JSON.

Penyimpanan JSON:

Data disimpan dalam format dictionary { "username": "password" }.

json.dump mengubah dictionary Python menjadi teks di file users.json.

json.load mengubah teks di file kembali menjadi dictionary supaya bisa diproses kode Python.

Tips Estetik:

Padding (pady, padx): Memberikan jarak antar elemen agar tidak "berdempetan".

Warna Modern: Menggunakan kode hex seperti #1877f2 (biru Facebook) dan background soft #f0f2f5.

Relief & Border: Menghilangkan border default (bd=0) dan menggunakan highlightthickness untuk membuat kotak input yang lebih modern (flat design).
