import argparse

parser = argparse.ArgumentParser()
parser.add_argument("print", type=str, nargs='?',default="y", help="message to print")
args = parser.parse_args()

try:
    while True:
    	print(args.print)
except KeyboardInterrupt:
    print('')