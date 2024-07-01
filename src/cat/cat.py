import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", action="store_true", help="Show line numbers")
parser.add_argument("file", type=str, help="File to read")
args = parser.parse_args()
try:
	with open (args.file) as file:
    	 lines = file.readlines()
except FileNotFoundError:
	print("That file was not found")

for i, line in enumerate(lines):
	if args.number:
		print(i+1 , end= ' ')
	print(line, end= '')
