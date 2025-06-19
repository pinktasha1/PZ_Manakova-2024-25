#Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
#Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка A.

import tkinter as tk
from tkinter import messagebox

def calculate_remainder():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())

        if a <= 0 or b <= 0:
            raise ValueError("A и B должны быть положительными числами.")
        if a <= b:
            raise ValueError("A должно быть больше B.")

        remainder = a % b
        label_result.config(text=f"Незанятая часть: {remainder}")
    except ValueError as e:
        messagebox.showerror("Ошибка ввода", str(e))


root = tk.Tk()
root.title("Незанятая часть отрезка")
root.geometry("320x220")
root.configure(bg="#e0e0e0")

label_a = tk.Label(root, text="Введите A:", bg="#e0e0e0")
label_a.pack(pady=(15, 0))
entry_a = tk.Entry(root, width=20)
entry_a.pack()

label_b = tk.Label(root, text="Введите B:", bg="#e0e0e0")
label_b.pack(pady=(10, 0))
entry_b = tk.Entry(root, width=20)
entry_b.pack()

btn_calc = tk.Button(root, text="Вычислить", command=calculate_remainder, bg="#4a90e2", fg="white")
btn_calc.pack(pady=15)

label_result = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#e0e0e0")
label_result.pack()

root.mainloop()