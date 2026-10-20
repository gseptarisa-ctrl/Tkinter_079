import tkinter as tk
from tkinter import ttk, messagebox

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x780")
root.resizable(False, False)
root.configure(bg="#4938C4")

# Variabel untuk menyimpan input nilai
nilai_vars = []

# Judul aplikasi
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold"),
    bg=warna_bg,
    fg=warna_putih
)
judul.pack(pady=(30, 35))

# Warna aplikasi
warna_bg = "#4938C4"
warna_input = "#7164D8"
warna_putih = "#FFFFFF"

# Bingkai utama
frame = tk.Frame(root, bg="white", padx=25, pady=20)
frame.pack(padx=25, pady=20, fill="both", expand=True)

