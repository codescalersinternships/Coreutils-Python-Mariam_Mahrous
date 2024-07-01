import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--omit_new_line", action="store_true", help="omit new line numbers")
parser.add_argument('rest', nargs=argparse.REMAINDER)
args = parser.parse_args()

if len(args.rest)>0 :
	content = " ".join(args.rest)
	if args.omit_new_line:
		print(content, end= '')
	else:
		print(content)
