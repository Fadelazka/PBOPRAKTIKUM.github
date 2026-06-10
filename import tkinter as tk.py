import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# Konfigurasi Database
USER_FILE = "users_subsidi.json"

# --- FUNGSI MANAJEMEN DATA ---

def load_data(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as f:
        return json.load(f)

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# --- LOGIKA AUTENTIKASI (Tugas Mandiri A) ---

def register():
    user = entry_user.get().strip()
    pwd = entry_pwd.get().strip()
    
    # Validasi Kolom Kosong
    if user == "" or pwd == "":
        messagebox.showwarning("Peringatan", "Kolom tidak boleh kosong!")
        return

    users = load_data(USER_FILE)
    if user in users:
        messagebox.showerror("Error", "Username sudah terdaftar!")
    else:
        users[user] = pwd
        save_data(USER_FILE, users)
        messagebox.showinfo("Sukses", "Akun Petugas Berhasil Dibuat!")

def login():
    user = entry_user.get().strip()
    pwd = entry_pwd.get().strip()

    if user == "" or pwd == "":
        messagebox.showwarning("Peringatan", "Username dan Password wajib diisi!")
        return

    users = load_data(USER_FILE)
    if users.get(user) == pwd:
        messagebox.showinfo("Login Berhasil", f"Selamat Datang, {user}!")
        buka_dashboard(user) # Pindah ke Dashboard
    else:
        messagebox.showerror("Gagal", "Username atau Password salah!")

# --- HALALMAN DASHBOARD (Tugas Mandiri B - Fitur Detail) ---

def buka_dashboard(petugas):
    # Sembunyikan jendela login
    root.withdraw()
    
    dash = tk.Toplevel()
    dash.title(f"Dashboard Distribusi Pupuk - Petugas: {petugas}")
    dash.geometry("900x600")
    dash.configure(bg="#f4f7f6")

    # --- SIDEBAR ---
    sidebar = tk.Frame(dash, bg="#2d5a27", width=200) # Hijau Tua Pertanian
    sidebar.pack(side="left", fill="y")

    tk.Label(sidebar, text="E-PUPUK", font=("Helvetica", 16, "bold"), 
             bg="#2d5a27", fg="white", pady=20).pack()

    # --- KONTEN UTAMA ---
    main_frame = tk.Frame(dash, bg="white", padx=20, pady=20)
    main_frame.pack(side="right", expand=True, fill="both")

    def show_content(title):
        # Bersihkan konten lama
        for widget in main_frame.winfo_children():
            widget.destroy()
        
        tk.Label(main_frame, text=title, font=("Helvetica", 18, "bold"), 
                 bg="white", fg="#2d5a27").pack(anchor="w", pady=(0, 20))

        if title == "Cek NIK Petani":
            render_cek_nik()
        elif title == "Stok Gudang":
            render_stok()
        elif title == "Input Distribusi":
            render_distribusi()

    # --- SUB-FITUR DETAIL ---
    
    def render_cek_nik():
        tk.Label(main_frame, text="Masukkan NIK Petani:", bg="white").pack(anchor="w")
        nik_entry = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
        nik_entry.pack(anchor="w", pady=5)
        
        def cek():
            nik = nik_entry.get()
            if nik == "12345": # Simulasi data
                messagebox.showinfo("Hasil", "NIK Terdaftar: Bpk. Raihan (Kelompok Tani Madiun)")
            else:
                messagebox.showwarning("Hasil", "NIK Tidak Terdaftar dalam RDKK!")
        
        tk.Button(main_frame, text="Cek Status NIK", command=cek, bg="#2ecc71", fg="white").pack(anchor="w")

    def render_stok():
        # Tabel Stok Pupuk
        cols = ("Jenis Pupuk", "Sisa Stok (Ton)", "Status")
        tree = ttk.Treeview(main_frame, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
        
        data_stok = [("Urea", "45.0", "Tersedia"), ("NPK Phonska", "12.5", "Terbatas"), ("ZA", "30.2", "Tersedia")]
        for s in data_stok:
            tree.insert("", "end", values=s)
        tree.pack(fill="x")

    def render_distribusi():
        tk.Label(main_frame, text="Form Penyaluran Pupuk", bg="white", font=("Arial", 12, "italic")).pack(pady=10)
        # Form sederhana
        tk.Label(main_frame, text="Jumlah (Kg):", bg="white").pack(anchor="w")
        tk.Entry(main_frame).pack(anchor="w", pady=5)
        tk.Button(main_frame, text="Simpan Transaksi", bg="#2d5a27", fg="white").pack(anchor="w", pady=10)

    # Tombol Navigasi Sidebar
    nav_btns = [("Cek NIK Petani", "#2d5a27"), ("Stok Gudang", "#2d5a27"), ("Input Distribusi", "#2d5a27")]
    for text, color in nav_btns:
        tk.Button(sidebar, text=text, font=("Helvetica", 10, "bold"), bg=color, fg="white", 
                  bd=0, pady=10, cursor="hand2", command=lambda t=text: show_content(t)).pack(fill="x")

    # Logout
    tk.Button(sidebar, text="Keluar Sistem", bg="#c0392b", fg="white", 
              command=lambda: [dash.destroy(), root.deiconify()]).pack(side="bottom", fill="x", pady=20)

    show_content("Cek NIK Petani") # Default view

# --- UI LOGIN (SISTEM DISTRIBUSI) ---

root = tk.Tk()
root.title("Login Sistem Distribusi Pupuk")
root.geometry("400x500")
root.configure(bg="#f0f2f5")

# Container Card
card = tk.Frame(root, bg="white", padx=40, pady=40, bd=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=320, height=420)

# Header
tk.Label(card, text="PUPUK SUBSIDI", font=("Helvetica", 16, "bold"), bg="white", fg="#2d5a27").pack(pady=(0, 5))
tk.Label(card, text="Silakan Login Petugas", font=("Helvetica", 9), bg="white", fg="#777").pack(pady=(0, 25))

# Entry Fields
tk.Label(card, text="Username", bg="white", font=("Arial", 10)).pack(anchor="w")
entry_user = tk.Entry(card, font=("Arial", 11), bg="#f9f9f9", bd=1)
entry_user.pack(fill="x", ipady=5, pady=(5, 15))

tk.Label(card, text="Password", bg="white", font=("Arial", 10)).pack(anchor="w")
entry_pwd = tk.Entry(card, font=("Arial", 11), bg="#f9f9f9", bd=1, show="•")
entry_pwd.pack(fill="x", ipady=5, pady=(5, 20))

# Buttons
btn_lgn = tk.Button(card, text="LOGIN", command=login, bg="#2d5a27", fg="white", 
                    font=("Helvetica", 10, "bold"), bd=0, cursor="hand2", pady=8)
btn_lgn.pack(fill="x", pady=(0, 10))

btn_reg = tk.Button(card, text="Daftar Akun Baru", command=register, bg="#ecf0f1", fg="#2d5a27", 
                    font=("Helvetica", 9), bd=0, cursor="hand2")
btn_reg.pack(fill="x")

root.mainloop()