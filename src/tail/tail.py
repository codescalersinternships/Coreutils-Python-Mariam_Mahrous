import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int , default=10, help="Show line numbers")
parser.add_argument("file", type=str, help="File to read")
args = parser.parse_args()
try:
	with open (args.file) as file:
    	 lines = file.readlines()
except FileNotFoundError:
	print("That file was not found")

j = len(lines)-args.number
if j < 0:
	j=0
for i in range(j, len(lines)):
	print(lines[i], end= '')
