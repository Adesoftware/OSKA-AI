import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time

from ollama_client import ask_oska
# ----------------------------
# Main Window
# ----------------------------
root = tk.Tk()
root.title("OSKA AI")
root.geometry("950x700")
root.configure(bg="#F3F6FB")
root.resizable(True, True)
# ----------------------------
# Generate Response
# ----------------------------

def generate_response():

    prompt = input_box.get("1.0", tk.END).strip()

    if prompt == "":
        status.config(text="Please enter a request.", fg="red")
        return

    output_box.delete("1.0", tk.END)

    generate_btn.config(state="disabled")

    threading.Thread(
        target=run_ai,
        args=(prompt,),
        daemon=True
    ).start()


def run_ai(prompt):

    start = time.time()


    start = time.time()

    animation = [
        "Analyzing your request.",
        "Analyzing your request..",
        "Analyzing your request..."
    ]

    for i in range(3):
        status.config(
            text=animation[i],
            fg="blue"
        )
        time.sleep(0.4)

    answer = ask_oska(prompt)
    

    answer = ask_oska(prompt)

    elapsed = round(time.time() - start, 1)

    root.after(0, lambda: output_box.delete("1.0", tk.END))
    root.after(0, lambda: output_box.insert(tk.END, answer))
    root.after(0, lambda: status.config(
        text=f"✓ Completed in {elapsed} seconds",
        fg="green"
    ))
    root.after(0, lambda: generate_btn.config(state="normal"))

    for i in range(3):
        status.config(
            text=animation[i],
            fg="blue"
        )
        time.sleep(0.4)

    answer = ask_oska(prompt)

    elapsed = round(time.time() - start,1)

    output_box.insert(tk.END, answer)

    status.config(
        text=f"✓ Completed in {elapsed} seconds",
        fg="green"
    )

    generate_btn.config(state="normal")
# ----------------------------
# Header
# ----------------------------
header = tk.Frame(root, bg="#0B4F9C", height=90)
header.pack(fill="x")

title = tk.Label(
    header,
    text="OSKA AI",
    bg="#0B4F9C",
    fg="white",
    font=("Segoe UI", 24, "bold")
)
title.pack(pady=(15, 0))

subtitle = tk.Label(
    header,
    text="Enterprise Intelligence Without the Cloud",
    bg="#0B4F9C",
    fg="white",
    font=("Segoe UI", 11)
)
subtitle.pack()

# ----------------------------
# Main Container
# ----------------------------
main = tk.Frame(root, bg="#F3F6FB")
main.pack(fill="both", expand=True, padx=20, pady=20)

# Feature
tk.Label(
    main,
    text="Select Feature",
    font=("Segoe UI", 11, "bold"),
    bg="#F3F6FB"
).pack(anchor="w")

feature = ttk.Combobox(
    main,
    values=[
        "Business Letter",
        "Memo Generator",
        "Text Summarizer",
        "General AI Chat"
    ],
    state="readonly",
    width=35
)
feature.current(0)
feature.pack(anchor="w", pady=(5, 15))

# Input
tk.Label(
    main,
    text="Enter your request",
    font=("Segoe UI", 11, "bold"),
    bg="#F3F6FB"
).pack(anchor="w")

input_box = scrolledtext.ScrolledText(
    main,
    height=7,
    font=("Segoe UI", 10)
)
input_box.pack(fill="x", pady=8)

# Buttons
button_frame = tk.Frame(main, bg="#F3F6FB")
button_frame.pack(fill="x", pady=10)

generate_btn = tk.Button(
    button_frame,
    text="Generate",
    bg="#0B4F9C",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=15,
    command=generate_response
)
generate_btn.pack(side="left", padx=5)


clear_btn = tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=lambda: (
        input_box.delete("1.0", tk.END),
        output_box.delete("1.0", tk.END),
        status.config(text="Ready", fg="green")
    )
)

clear_btn.pack(side="left", padx=5)

copy_btn = tk.Button(
    button_frame,
    text="Copy",
    width=12,
    command=lambda: root.clipboard_append(output_box.get("1.0", tk.END))
)
copy_btn.pack(side="left", padx=5)

# Status
status = tk.Label(
    main,
    text="Ready",
    fg="green",
    bg="#F3F6FB",
    font=("Segoe UI", 10)
)
status.pack(anchor="w", pady=5)

# Output
tk.Label(
    main,
    text="OSKA Response",
    font=("Segoe UI", 11, "bold"),
    bg="#F3F6FB"
).pack(anchor="w")

output_box = scrolledtext.ScrolledText(
    main,
    height=15,
    font=("Segoe UI", 10)
)
output_box.pack(fill="both", expand=True, pady=8)

root.mainloop()