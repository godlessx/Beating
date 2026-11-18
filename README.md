# Beats — Two Close Frequencies

## Overview

This project demonstrates the phenomenon of beats produced by adding two sinusoidal waves with slightly different frequencies.

Using Python, NumPy, and Matplotlib, the program generates two waves, calculates their sum, and visualizes the resulting waveform along with its amplitude envelope.

## Physics

When two sinusoidal waves with slightly different frequencies interfere, their superposition produces a phenomenon called **beats**.

The individual waves are described by:

$$y_1(t)=\sin(2\pi f_1t)$$

$$y_2(t)=\sin(2\pi f_2t)$$

The resulting waveform is obtained by adding the two waves:

$$y(t)=y_1(t)+y_2(t)$$

The beat frequency is calculated as:

$$f_{\text{beats}}=|f_1-f_2|$$

In this simulation, the frequencies are:

- First wave: 10 Hz
- Second wave: 12 Hz
- Beat frequency: 2 Hz

The amplitude envelope is described by:

$$A(t)=2\left|\cos\left(\pi(f_1-f_2)t\right)\right|$$

This envelope illustrates the periodic increase and decrease in the amplitude of the resulting waveform.

## Features

- Generates two sinusoidal waves with different frequencies.
- Calculates the beat frequency.
- Computes the resulting waveform through superposition.
- Calculates the upper and lower amplitude envelopes.
- Visualizes the waves using separate plots.

## Visualization

The program generates three plots:

1. **First Wave** — the sinusoidal wave with a frequency of 10 Hz.
2. **Second Wave** — the sinusoidal wave with a frequency of 12 Hz.
3. **Sum of Two Waves** — the resulting waveform with its upper and lower amplitude envelopes.

## Technologies Used

- Python
- NumPy
- Matplotlib

## How to Run

1. Clone the repository.
2. Make sure Python is installed.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Run the program:

```bash
python beats.py
```

## Purpose

This project was created to explore the connection between mathematical functions, physics, and programming through numerical computation and data visualization.
