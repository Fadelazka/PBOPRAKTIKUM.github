Penjelasan praktikum :

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



Penjelasan Mandiri :

Struktur Sidebar & Main Content:

Saya menggunakan dua Frame utama di Dashboard: sidebar (kiri) dan main_frame (kanan).

Fungsi show_content() sangat penting. Fungsinya adalah menghapus apapun yang ada di tengah layar (widget.destroy()) dan menggantinya dengan tampilan fitur baru saat tombol diklik. Ini membuat aplikasi terasa dinamis seperti aplikasi web.

Penggunaan ttk.Treeview:

Untuk fitur Stok Gudang, saya menggunakan Treeview. Ini adalah widget standar Tkinter untuk menampilkan data berbentuk tabel/grid agar terlihat rapi.

Logika Transisi:

root.withdraw() digunakan untuk menyembunyikan jendela login saat dashboard terbuka, dan root.deiconify() digunakan untuk memunculkan kembali jendela login jika user menekan tombol "Keluar Sistem".

Tema Warna (Agriculture Theme):

Warna utama adalah #2d5a27 (Deep Green). Ini memberikan kesan sistem resmi pertanian yang profesional dibandingkan hanya menggunakan warna standar abu-abu Tkinter.

Validasi Mandiri:

Input divalidasi menggunakan .strip(). Fungsi ini akan menghapus spasi kosong. Jadi, jika user hanya menekan "spasi" tanpa karakter, sistem akan tetap menganggapnya kosong dan memunculkan peringatan.
