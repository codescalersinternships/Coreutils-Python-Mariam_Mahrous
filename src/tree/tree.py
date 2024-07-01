import argparse , sys , os

def visit(path, depth, max_depth):
    files = os.listdir(path)
    for file in files:
        printLength(depth +1)
        print(file)
        if os.path.isdir(path+file) and depth < max_depth:
            visit(path+file, depth + 1, max_depth)	

	
def printLength(depth):
	for _ in range (depth - 1) :
		print("  ", end="")
	print("|__", end="")


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--depth", type= int , default=sys.maxsize,  nargs='?', help="Depth of Directories")
args = parser.parse_args()
visit("./", 0, args.depth)