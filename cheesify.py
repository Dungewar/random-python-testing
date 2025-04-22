#!/home/dungewar/PycharmProjects/RandomTesting/.venv/bin/python3
import argparse
import numpy as np
import sounddevice as sd

parser = argparse.ArgumentParser(description="MELT THE TERMINAL WITH CHEESE.")

parser.add_argument("-d", "--display", help="Displays the cheese", action="store_true")
parser.add_argument("-b", "--bell", help="Rings the school bells", action="store", const=3, nargs='?')
# parser.add_argument("-p", "--play", help="Plays a little tune", action="store_true")

parser.add_argument("-a", "--add", help="Adds 2 numbers together", action="store_true")
parser.add_argument("-s", "--subtract", help="Subtracts 2 numbers together", action="store_true")
parser.add_argument("-m", "--multiply", help="Multiplies 2 numbers together", action="store_true")
parser.add_argument("-v", "--divide", help="Divides 2 numbers together", action="store_true")

parser.add_argument("val1", type=float, nargs='?', help="The first value")
parser.add_argument("val2", type=float, nargs='?', help="The second value")
parser.add_argument("val3", type=float, nargs='?', help="The third value")


args = parser.parse_args()


def play_tone(frequency=400, duration=1.0, sample_rate=44100, volume=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t) * volume
    sd.play(tone, sample_rate)
    sd.wait()  # Block until done


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

if args.bell:
    time: float = float(args.bell)
    print(time)
    play_tone(frequency=494, duration=time)

def require_args(num: int):
    if num > num_args():
        raise argparse.ArgumentTypeError(f"Too few arguments, you need {num} arg{"s" if num > 1 else ""}")
    # if num == 3 and num_args() < 3:
    #     raise OSError('You must provide three values')
    # elif num == 2 and num_args() < 2:
    #     raise OSError('You must provide two values')
    # elif num == 1 and num_args() < 1:
    #     raise OSError('You must provide one value')

def num_args() -> int:
    if args.val1:
        if args.val2:
            if args.val3:
                return 3
            return 2
        return 1
    return 0


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