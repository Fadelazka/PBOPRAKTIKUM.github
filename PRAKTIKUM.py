import tkinter as tk
from tkinter import messagebox
import json
import os

# Konfigurasi File Database
FILE_NAME = "users.json"

# --- FUNGSI LOGIKA (BACKEND) ---

def load_users():
    """Memuat data pengguna dari file JSON."""
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    """Menyimpan data pengguna ke file JSON."""
    with open(FILE_NAME, "w") as f:
        json.dump(users, f, indent=4)

def register():
    """Logika pendaftaran akun baru dengan validasi."""
    user = entry_user.get().strip()
    pwd = entry_pwd.get().strip()
    users = load_users()

    # Validasi Tugas Mandiri A: Kolom tidak boleh kosong
    if user == "" or pwd == "":
        messagebox.showwarning("Peringatan", "Username dan Password tidak boleh kosong!")
        return

    if user in users:
        messagebox.showerror("Error", "Username sudah terdaftar!")
    else:
        users[user] = pwd
        save_users(users)
        messagebox.showinfo("Success", f"Registrasi Berhasil!\nSelamat bergabung, {user}!")
        # Bersihkan kolom setelah daftar
        entry_user.delete(0, tk.END)
        entry_pwd.delete(0, tk.END)

def login():
    """Logika login dengan validasi dan pindah halaman."""
    user = entry_user.get().strip()
    pwd = entry_pwd.get().strip()
    users = load_users()

    # Validasi Tugas Mandiri A: Kolom tidak boleh kosong
    if user == "" or pwd == "":
        messagebox.showwarning("Peringatan", "Silakan isi Username dan Password!")
        return

    if users.get(user) == pwd:
        messagebox.showinfo("Login Berhasil", f"Selamat Datang, {user}!")
        buka_halaman_utama(user) # Tugas Mandiri B
    else:
        messagebox.showerror("Login Gagal", "Username atau Password Salah!")

# --- FUNGSI ANTARMUKA HALAMAN BARU (TUGAS MANDIRI B) ---

def buka_halaman_utama(username):
    """Membuat jendela baru (Dashboard) setelah login sukses."""
    # Sembunyikan jendela login (opsional agar estetik)
    # root.withdraw() 

    dashboard = tk.Toplevel(root)
    dashboard.title("Dashboard Utama")
    dashboard.geometry("400x300")
    dashboard.configure(bg="#ffffff") # Background Putih Bersih

    # Styling Dashboard
    tk.Label(dashboard, text="DASHBOARD UTAMA", font=("Helvetica", 16, "bold"), 
             bg="#ffffff", fg="#333333").pack(pady=(40, 10))
    
    tk.Label(dashboard, text=f"Halo, {username}!", font=("Helvetica", 12), 
             bg="#ffffff", fg="#666666").pack(pady=5)
    
    tk.Label(dashboard, text="Anda berhasil masuk ke sistem.", font=("Helvetica", 10), 
             bg="#ffffff", fg="#777777").pack(pady=20)

    btn_logout = tk.Button(dashboard, text="Keluar", command=dashboard.destroy, 
                          bg="#e74c3c", fg="white", font=("Helvetica", 10, "bold"),
                          width=15, bd=0, cursor="hand2")
    btn_logout.pack(pady=20)

# --- SETUP UI UTAMA (ESTETIK) ---

root = tk.Tk()
root.title("Sistem Informasi")
root.geometry("350x450")
root.configure(bg="#f0f2f5") # Warna background abu-abu muda modern

# Font Styles
font_label = ("Helvetica", 10)
font_title = ("Helvetica", 18, "bold")

# Container Utama (Agar terlihat seperti Card)
frame_card = tk.Frame(root, bg="white", padx=30, pady=30, highlightthickness=1, highlightbackground="#dddddd")
frame_card.place(relx=0.5, rely=0.5, anchor="center", width=300, height=400)

# Judul
tk.Label(frame_card, text="Welcome", font=font_title, bg="white", fg="#1c1e21").pack(pady=(0, 20))

# Input Username
tk.Label(frame_card, text="Username", font=font_label, bg="white", fg="#606770").pack(anchor="w")
entry_user = tk.Entry(frame_card, font=("Helvetica", 11), bg="#f5f6f7", bd=0, highlightthickness=1, highlightbackground="#ccd0d5")
entry_user.pack(fill="x", ipady=5, pady=(5, 15))

# Input Password
tk.Label(frame_card, text="Password", font=font_label, bg="white", fg="#606770").pack(anchor="w")
entry_pwd = tk.Entry(frame_card, font=("Helvetica", 11), bg="#f5f6f7", bd=0, highlightthickness=1, highlightbackground="#ccd0d5", show="•")
entry_pwd.pack(fill="x", ipady=5, pady=(5, 20))

# Tombol Login
btn_login = tk.Button(frame_card, text="Log In", command=login, 
                      bg="#1877f2", fg="white", font=("Helvetica", 11, "bold"), 
                      bd=0, cursor="hand2", activebackground="#166fe5", activeforeground="white")
btn_login.pack(fill="x", ipady=7, pady=(0, 10))

# Garis Pembatas
separator = tk.Frame(frame_card, height=1, bg="#dadde1")
separator.pack(fill="x", pady=10)

# Tombol Register
btn_reg = tk.Button(frame_card, text="Create New Account", command=register, 
                     bg="#42b72a", fg="white", font=("Helvetica", 10, "bold"), 
                     bd=0, cursor="hand2", activebackground="#36a420", activeforeground="white")
btn_reg.pack(fill="x", ipady=7)

root.mainloop()