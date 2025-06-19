import tkinter as tk
from tkinter import ttk, messagebox


def send_message():
    name = entry_name.get()
    email = entry_email.get()
    message = text_message.get("1.0", tk.END).strip()
    subject = combo_subject.get()

    if not name or not email or not message:
        messagebox.showwarning("Warning", "Please fill all entries.")
        return

    messagebox.showinfo("Sent", "Message sent successfully!")


root = tk.Tk()
root.title("Contact Form")
root.geometry("400x400")
root.configure(bg="#bfbfbf")

frame = tk.Frame(root, bg="#d3d3d3", bd=2, relief=tk.FLAT)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label_title = tk.Label(frame, text="Contact Form", font=("Helvetica", 16, "bold"), bg="#d3d3d3")
label_title.grid(row=0, column=0, columnspan=2, pady=(10, 0))

label_subtitle = tk.Label(frame, text="Please fill all entries.", font=("Helvetica", 10), bg="#d3d3d3")
label_subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 10))

label_name = tk.Label(frame, text="Name :", bg="#d3d3d3")
label_name.grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=2, column=1, pady=5)

label_email = tk.Label(frame, text="Email :", bg="#d3d3d3")
label_email.grid(row=3, column=0, sticky=tk.E, padx=10, pady=5)
entry_email = tk.Entry(frame, width=30)
entry_email.grid(row=3, column=1, pady=5)

label_message = tk.Label(frame, text="Message :", bg="#d3d3d3")
label_message.grid(row=4, column=0, sticky=tk.NE, padx=10, pady=5)
text_message = tk.Text(frame, width=30, height=5)
text_message.grid(row=4, column=1, pady=5)

label_subject = tk.Label(frame, text="Subject :", bg="#d3d3d3")
label_subject.grid(row=5, column=0, sticky=tk.E, padx=10, pady=5)
combo_subject = ttk.Combobox(frame, values=["Product Inquiry", "Support", "Feedback", "Other"], width=28)
combo_subject.set("Product Inquiry")
combo_subject.grid(row=5, column=1, pady=5)

btn_send = tk.Button(frame, text="Send", width=10, bg="#555555", fg="white", relief=tk.RAISED, command=send_message)
btn_send.grid(row=6, column=0, columnspan=2, pady=15)

root.mainloop()