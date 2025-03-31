import numpy as np
from scipy.io.wavfile import write
import os

# Ustawienia folderu wyjściowego
output_dir = "sounds"
os.makedirs(output_dir, exist_ok=True)

# Funkcja do generowania tonu
def generate_tone(freq, duration=1.0, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = amplitude * np.sin(2 * np.pi * freq * t)
    return np.int16(tone * 32767)

# Lista dźwięków do testu
notes_freqs = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88,
    "C5": 523.25
}

# 1. Rozpoznawanie wysokości – para dźwięków
write(os.path.join(output_dir, "high_low_1.wav"), 44100,
      np.concatenate([generate_tone(notes_freqs["C4"]), generate_tone(notes_freqs["E4"])]))
write(os.path.join(output_dir, "high_low_2.wav"), 44100,
      np.concatenate([generate_tone(notes_freqs["G4"]), generate_tone(notes_freqs["C4"])]))

# 2. Pamięć muzyczna – bazowa melodia i warianty
melody_base = np.concatenate([generate_tone(notes_freqs[n], 0.5) for n in ["C4", "D4", "E4", "F4"]])
melody_a = melody_base.copy()
melody_b = np.concatenate([generate_tone(notes_freqs[n], 0.5) for n in ["C4", "D4", "F4", "E4"]])
melody_c = np.concatenate([generate_tone(notes_freqs[n], 0.5) for n in ["E4", "D4", "C4", "F4"]])

write(os.path.join(output_dir, "melody_base.wav"), 44100, melody_base)
write(os.path.join(output_dir, "melody_a.wav"), 44100, melody_a)
write(os.path.join(output_dir, "melody_b.wav"), 44100, melody_b)
write(os.path.join(output_dir, "melody_c.wav"), 44100, melody_c)

# 3. Rytm – proste kliknięcia w różnych rytmach
def generate_click_rhythm(pattern, duration=0.25, sample_rate=44100):
    click = generate_tone(1000, 0.05, sample_rate, 1.0)
    silence = np.zeros(int(sample_rate * duration), dtype=np.int16)
    rhythm = []
    for char in pattern:
        if char == 'x':
            rhythm.append(click)
        else:
            rhythm.append(silence)
    return np.concatenate(rhythm)

rhythm1 = generate_click_rhythm("x-x--x-x")
write(os.path.join(output_dir, "rhythm_1.wav"), 44100, rhythm1)

# 4. Intonacja – pojedynczy dźwięk
write(os.path.join(output_dir, "note_c.wav"), 44100, generate_tone(notes_freqs["C4"]))

# 5. Interwał – C do E
interval = np.concatenate([generate_tone(notes_freqs["C4"]), generate_tone(notes_freqs["E4"])])
write(os.path.join(output_dir, "interval_c_to_e.wav"), 44100, interval)

# 6. Instrument – symulacja dźwięku (niestety syntetyczne brzmienie, np. skrzypce = wysoka sinusoida z tremolo)
def generate_violin_like_note(freq, duration=1.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    vibrato = 5 * np.sin(2 * np.pi * 5 * t)  # tremolo effect
    tone = 0.5 * np.sin(2 * np.pi * (freq + vibrato) * t)
    return np.int16(tone * 32767)

violin = generate_violin_like_note(notes_freqs["G4"])
write(os.path.join(output_dir, "instrument_violin.wav"), 44100, violin)