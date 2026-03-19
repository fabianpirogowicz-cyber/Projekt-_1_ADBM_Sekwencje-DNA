import tkinter as tk
from tkinter import filedialog, messagebox
from dna_analysis import load_sequence, motif_statistics
from visualization import plot_motif_positions, bar_plot
from export import export_to_csv

sequence = ""


def load_file():
    global sequence

    path = filedialog.askopenfilename()

    if not path:
        return

    sequence = load_sequence(path)

    label.config(text="Sekwencja załadowana")


def analyze():

    global sequence

    if sequence == "":
        messagebox.showerror("Błąd", "Najpierw wczytaj plik DNA")
        return

    motif = entry.get()

    if motif == "":
        messagebox.showerror("Błąd", "Podaj motyw DNA")
        return

    data = motif_statistics(sequence, motif)

    result_label.config(
        text=f"Liczba wystąpień: {data['count']}"
    )

    plot_motif_positions(len(sequence), data["positions"])
    bar_plot(data["count"])

    export_to_csv(data)


def start_gui():

    global entry, label, result_label

    root = tk.Tk()
    root.title("DNA Motif Analyzer")
    root.geometry("300x200")

    label = tk.Label(root, text="Wybierz plik DNA")
    label.pack()

    btn = tk.Button(root, text="Wczytaj plik", command=load_file)
    btn.pack()

    entry = tk.Entry(root)
    entry.pack()

    analyze_btn = tk.Button(root, text="Analizuj motyw", command=analyze)
    analyze_btn.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()