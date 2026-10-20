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
