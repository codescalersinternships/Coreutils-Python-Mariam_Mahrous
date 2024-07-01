import argparse , os

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int , default=10, help="Show line numbers")
parser.add_argument("file", type=str, help="File to read")
args = parser.parse_args()
try:
	with open (args.file) as file:
    	 lines = file.readlines()
except FileNotFoundError:
	print("That file was not found")

for i, line in enumerate(lines):
	if args.number <= i:
		os._exit(1)
	print(line, end= '')
