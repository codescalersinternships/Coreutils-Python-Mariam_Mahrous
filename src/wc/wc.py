import argparse , os

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--show_lines", action="store_true", help="Show line numbers")
parser.add_argument("-w", "--show_words", action="store_true", help="Show words numbers")
parser.add_argument("-c", "--show_chars", action="store_true", help="Show chars numbers")
parser.add_argument("file", type=str, help="File to read")
args = parser.parse_args()
try:
	with open (args.file) as file:
		content = file.read()
		lines_number = len(content.split('\n'))
		chars_number = len(content)
		words_number = len(content.split())

		if args.show_lines:
			print(lines_number , end= ' ')
		if args.show_words:
			print(words_number , end= ' ')
		if args.show_chars:
			print(chars_number , end= ' ')
		if not (args.show_lines or args.show_words or args.show_chars):
			print(lines_number, words_number, chars_number, end=' ')
		print(args.file , end="")
except FileNotFoundError:
	print("file not found")




