# Rayleigh Fading Channels Simulator

A graphical Python simulator for visualizing time-varying Rayleigh fading channels using the Clarke & Gans model (Jakes’ Sum-of-Sinusoids method).  
This tool allows users to define multiple channel scenarios and customize their appearance in real time via an intuitive GUI.

## 📌 Overview

Rayleigh fading is a statistical model describing the rapid fluctuations of wireless signals in environments without a dominant line-of-sight path.  
This simulator uses the **Clarke and Gans model**, which generates realistic Rayleigh fading waveforms using a sum-of-sinusoids approach.

> ✅ Supports multiple case comparison, custom line color and width, real-time plotting.

---

## 🖥️ GUI Preview

![image](https://github.com/user-attachments/assets/c7999af7-b8d5-487d-9834-0502401c6cda)


---

## 🔧 Features

- ✅ Generate Rayleigh fading envelopes based on carrier frequency and velocity
- ✅ Configure **multiple cases** with independent style parameters (color, linewidth)
- ✅ Real-time plotting using `matplotlib` inside `tkinter` interface
- ✅ Implements Clarke & Gans / Jakes model using sum-of-sinusoids
- ✅ Educational tool for wireless communications and signal modeling

---

## 📦 Requirements

- Python 3.7+
- `numpy`
- `matplotlib`
- `tkinter` (built-in with most Python distributions)

You can install required packages with:

```bash
pip install numpy matplotlib
