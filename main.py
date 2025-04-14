import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

def clarke_rayleigh_fading(fc, v, duration=1.0, fs=1000, N=16):
    c = 3e8  # speed of light [m/s]
    v_mps = v * 1000 / 3600  # convert km/h to m/s
    fd = (v_mps / c) * fc * 1e9  # Doppler frequency in Hz

    t = np.arange(0, duration, 1 / fs)

    theta = 2 * np.pi * np.arange(1, N + 1) / (N + 1)  # equally spaced AoA
    phi = 2 * np.pi * np.random.rand(N)  # random phase

    real_part = np.zeros_like(t)
    imag_part = np.zeros_like(t)

    for n in range(N):
        wn = 2 * np.pi * fd * np.cos(theta[n])
        real_part += np.cos(wn * t + phi[n])
        imag_part += np.sin(wn * t + phi[n])

    real_part *= np.sqrt(2 / N)
    imag_part *= np.sqrt(2 / N)

    h = real_part + 1j * imag_part
    return t, np.abs(h)


def simulate_all():
    all_inputs = []
    for row in input_rows:
        try:
            fc = float(row[0].get())
            v = float(row[1].get())
            all_inputs.append((fc, v))
        except ValueError:
            messagebox.showerror("입력 오류", "숫자 값을 올바르게 입력해주세요.")
            return

    plt.figure(figsize=(12, 6), dpi=120)

    for fc, v in all_inputs:
        t, fading = clarke_rayleigh_fading(fc, v)
        label = f"fc = {fc} GHz, v = {v} km/h"
        plt.plot(t, fading, label=label, linewidth=2)

    plt.title("Rayleigh Fading Channels (Sum-of-Sinusoids Model)", fontsize=16)
    plt.xlabel("Time (s)", fontsize=14)
    plt.ylabel("Amplitude", fontsize=14)
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.legend(fontsize=12, loc='best')
    plt.tight_layout()
    plt.show()


def add_input_row():
    row_idx = len(input_rows) + 1
    fc_entry = ttk.Entry(main_frame, width=15)
    v_entry = ttk.Entry(main_frame, width=15)
    fc_entry.grid(row=row_idx, column=0, padx=5, pady=5)
    v_entry.grid(row=row_idx, column=1, padx=5, pady=5)
    fc_entry.insert(0, "2.7")
    v_entry.insert(0, "120")
    input_rows.append((fc_entry, v_entry))

# GUI 구성
root = tk.Tk()
root.title("Rayleigh Fading Channel Simulator")

style = ttk.Style()
style.theme_use('clam')

title_label = ttk.Label(root, text="Rayleigh Fading Channel Simulator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

main_frame = ttk.Frame(root)
main_frame.pack(padx=10, pady=10)

# 헤더
ttk.Label(main_frame, text="Carrier Frequency (GHz)").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(main_frame, text="Velocity (km/h)").grid(row=0, column=1, padx=5, pady=5)

input_rows = []
add_input_row()  # 첫 줄 추가

# 버튼 영역
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Add Case", command=add_input_row)
add_button.grid(row=0, column=0, padx=5)

simulate_button = ttk.Button(button_frame, text="Simulate All", command=simulate_all)
simulate_button.grid(row=0, column=1, padx=5)

root.mainloop()
