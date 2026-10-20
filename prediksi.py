import tkinter as tk
from tkinter import ttk, messagebox

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x780")
root.resizable(False, False)
root.configure(bg="#4938C4")

#Variabel untuk menyimpan input nilai
nilai_vars = []

#Judul aplikasi
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold"),
    bg=warna_bg,
    fg=warna_putih
)
judul.pack(pady=(30, 35))

#Warna aplikasi
warna_bg = "#4938C4"
warna_input = "#7164D8"
warna_putih = "#FFFFFF"

#Bingkai utama
frame_input = tk.Frame(root, bg=warna_bg)
frame_input.pack(padx=25)

# Membuat 10 label 
entries = []

for i in range(10):
    baris = tk.Frame(frame_input, bg=warna_bg)
    baris.pack(fill="x", pady=7)

    label = tk.Label(
        baris,
        text=f"Nilai Mata Pelajaran {i + 1}:",
        font=("Arial", 11, "bold"),
        bg=warna_bg,
        fg=warna_putih,
        width=23,
        anchor="w"
    )
    label.pack(side="left")

    entry = tk.Entry(
        baris,
        font=("Arial", 11),
        width=15,
        bg=warna_input,
        fg=warna_putih,
        insertbackground=warna_putih,
        relief="flat",
        justify="center"
    )
    entry.pack(side="left", ipady=4)

    entries.append(entry)

# Label pilihan jurusan
label_jurusan = tk.Label(
    root,
    text="Pilihan Jurusan Anda:",
    font=("Arial", 12, "bold"),
    bg=warna_bg,
    fg=warna_putih
)
label_jurusan.pack(pady=(35, 10))

# Pilihan jurusan
jurusan = ttk.Combobox(
    root,
    values=["Teknologi Informasi"],
    state="readonly",
    font=("Arial", 11),
    width=20,
    justify="center"
)
jurusan.pack()
jurusan.set("Teknologi Informasi")

# Fungsi hasil prediksi
def hasil_prediksi():
    # Hasil selalu Teknologi Informasi
    jurusan.set("Teknologi Informasi")

    messagebox.showinfo(
        "Hasil Prediksi",
        "Pilihan Prodi Anda: Teknologi Informasi"
    )

# Tombol hasil prediksi
tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi,
    font=("Arial", 12, "bold"),
    bg=warna_bg,
    fg=warna_putih,
    activebackground=warna_input,
    activeforeground=warna_putih,
    relief="solid",
    bd=2,
    cursor="hand2",
    padx=12,
    pady=7
)
tombol.pack(pady=35)

# Menjalankan aplikasi
root.mainloop()
