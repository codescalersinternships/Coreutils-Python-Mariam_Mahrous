import argparse , os

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--show_Lines", action="store_true", help="Show line numbers")
parser.add_argument("-w", "--show_Words", action="store_true", help="Show words numbers")
parser.add_argument("-c", "--show_Chars", action="store_true", help="Show chars numbers")
parser.add_argument("file", type=str, help="File to read")
args = parser.parse_args()
try:
	with open (args.file) as file:
    	 content = file.read()
except FileNotFoundError:
	print("file not found")

lines_number = len(content.split('\n'))
chars_number = len(content)
words_number = len(content.split())

if args.show_Lines:
	print(lines_number , end= ' ')
if args.show_Words:
	print(words_number , end= ' ')
if args.show_Chars:
	print(chars_number , end= ' ')
if not args.show_Lines and not args.show_Words and not args.show_Chars:
    print(lines_number, words_number, chars_number, end=' ')
print(args.file , end="")



