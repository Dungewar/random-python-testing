#!/home/dungewar/PycharmProjects/RandomTesting/.venv/bin/python3
import argparse
import time
from datetime import datetime, timedelta
import subprocess
import numpy as np
import sounddevice as sd

# === VOLUME CONTROL ===
def set_volume(percent: int):
    percent = max(0, min(100, percent))
    subprocess.run(["amixer", "sset", "Master", f"{percent}%"])

# === ARGPARSE ===
parser = argparse.ArgumentParser(description="MELT THE TERMINAL WITH CHEESE.")

parser.add_argument("-d", "--display", help="Displays the cheese", action="store_true")
parser.add_argument("-bd", "--belldelay", help="Rings the school bells", action="store", const=0, nargs='?')
parser.add_argument("-bt", "--belltime", help="Rings the school bells", action="store", const=0, nargs='?')
parser.add_argument("-a", "--add", help="Adds 2 numbers together", action="store_true")
parser.add_argument("-s", "--subtract", help="Subtracts 2 numbers together", action="store_true")
parser.add_argument("-m", "--multiply", help="Multiplies 2 numbers together", action="store_true")
parser.add_argument("-v", "--divide", help="Divides 2 numbers together", action="store_true")

parser.add_argument("val1", type=float, nargs='?')
parser.add_argument("val2", type=float, nargs='?')
parser.add_argument("val3", type=float, nargs='?')

args = parser.parse_args()

# === TONE FUNCTION ===
def play_tone(frequency=400, duration=1.0, sample_rate=44100, volume=1.0):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t) * volume
    sd.play(tone, sample_rate)
    sd.wait()  # Block until done

# === DISPLAY ===
if args.display:
    print("""
         _--"-.
      .-"      "-.
     |""--..      '-.
     |      ""--..   '-.
     |.-. .-".    ""--..".
     |'./  -_'  .-.      |
     |      .-. '.-'   .-'
     '--..  '.'    .-  -.
          ""--..   '_'   :
                ""--..   |
                      ""-' 
""")

# === BELL ===
if args.belldelay or args.belltime:
    if args.belldelay:
        delay_until_ring: float = float(args.belldelay)
        print(delay_until_ring)
        time.sleep(int(delay_until_ring))
    if args.belltime:
        target_time = datetime.strptime(args.belltime, "%H:%M").time()
        print(f"Ringing at {target_time.strftime('%H:%M')}")
        current_time = datetime.now()
        target_datetime = datetime.combine(current_time.date(), target_time)

        if target_datetime < current_time:
            target_datetime += timedelta(days=1)

        sleep_seconds = (target_datetime - current_time).total_seconds()
        print(f"Sleeping for {sleep_seconds} seconds")
        time.sleep(sleep_seconds)

    print("MAX VOLUME! 🧀🔊")
    set_volume(100)
    print("Playing bells...")
    play_tone(frequency=494, duration=3)
    print("SHUTTING DOWN VOLUME 🧀🤫")
    set_volume(0)

# === MATH ===
def require_args(num: int):
    if num > num_args():
        raise argparse.ArgumentTypeError(f"Too few arguments, you need {num} arg{"s" if num > 1 else ""}")

def num_args() -> int:
    return sum(1 for arg in (args.val1, args.val2, args.val3) if arg is not None)

if args.add:
    require_args(2)
    print(f"{args.val1} + {args.val2} = {args.val1 + args.val2}")

if args.subtract:
    require_args(2)
    print(f"{args.val1} - {args.val2} = {args.val1 - args.val2}")

if args.multiply:
    require_args(2)
    print(f"{args.val1} * {args.val2} = {args.val1 * args.val2}")

if args.divide:
    require_args(2)
    print(f"{args.val1} / {args.val2} = {args.val1 / args.val2}")
