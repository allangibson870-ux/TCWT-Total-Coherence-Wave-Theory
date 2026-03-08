import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

time_start = -10.0
time_end   =  10.0
num_steps  =  4000

hum_amplitude  = 1.0
hum_frequency  = 0.12

main_knot_amplitude = 2.0
main_knot_frequency = 0.25
main_knot_damping   = 0.04

sub_knot_amplitude        = 3.0
sub_knot_frequency        = 0.6
sub_knot_base_damping     = 0.06
sub_knot_extra_damping    = 0.10
sub_knot_center_time      = -2.0
sub_knot_width            =  1.0
sub_knot_threshold_factor =  0.7
sub_knot_post_freq_drop   =  0.4

def background_hum(t):
    return hum_amplitude * np.sin(2 * np.pi * hum_frequency * t)

def main_knot(t):
    damping = np.exp(-main_knot_damping * (t - time_start))
    return main_knot_amplitude * damping * np.sin(2 * np.pi * main_knot_frequency * t)

def sub_knot(t):
    envelope = np.exp(-0.5 * ((t - sub_knot_center_time) / sub_knot_width) ** 2)
    raw = sub_knot_amplitude * envelope
    threshold_value = sub_knot_threshold_factor * sub_knot_amplitude
    snapped = raw > threshold_value
    damping_rate = np.where(snapped,
                            sub_knot_base_damping + sub_knot_extra_damping,
                            sub_knot_base_damping)
    damping = np.exp(-damping_rate * (t - time_start))
    freq = np.where(snapped,
                    sub_knot_frequency - sub_knot_post_freq_drop,
                    sub_knot_frequency)
    return raw * damping * np.sin(2 * np.pi * freq * t)

def build_signal(t):
    hum = background_hum(t)
    main = main_knot(t)
    sub = sub_knot(t)
    total = hum + main + sub
    return hum, main, sub, total

def main():
    t = np.linspace(time_start, time_end, num_steps)
    hum, main, sub, total = build_signal(t)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor("white")

    axes[0].plot(total, t, color="black", linewidth=1.0, alpha=0.9)
    axes[0].plot(main, t, color="steelblue", linewidth=0.6, alpha=0.5)
    axes[0].plot(sub, t, color="crimson", linewidth=0.6, alpha=0.7)
    axes[0].set_title("Nested Spiral")
    axes[0].set_xlabel("Curvature / Wave Amplitude")
    axes[0].set_ylabel("Time parameter")
    axes[0].grid(alpha=0.2)

    axes[1].plot(t, total, color="black", linewidth=1.0, alpha=0.9, label="Total")
    axes[1].plot(t, main, color="steelblue", linewidth=0.6, alpha=0.5, label="Main knot")
    axes[1].plot(t, sub, color="crimson", linewidth=0.6, alpha=0.7, label="Sub-knot")
    axes[1].set_title("Waveform Components")
    axes[1].set_xlabel("Time parameter")
    axes[1].set_ylabel("Amplitude")
    axes[1].legend(loc="best")
    axes[1].grid(alpha=0.2)

    png_path = os.path.join(os.getcwd(), "$PNG_NAME")
    fig.tight_layout()
    fig.savefig(png_path, dpi=200, facecolor="white")
    plt.close(fig)

    print(f"Saved figure to: {png_path}")

if __name__ == "__main__":
    main()
