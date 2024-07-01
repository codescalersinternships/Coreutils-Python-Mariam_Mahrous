import argparse , sys , os

def visit(path, depth, max_depth):
    try:
        files = os.listdir(path)
        if depth < max_depth :
            for file in files:
                printLength(depth +1)
                print(file)
                if os.path.isdir(os.path.join(path, file)):
                    visit(os.path.join(path, file), depth + 1, max_depth)	
    except PermissionError:
	    print("access denied")
    except FileNotFoundError:
	    print("file not found") 

	
def printLength(depth):
	for _ in range (depth - 1) :
		print("  ", end="")
	print("|__", end="")


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--depth", type= int , default=sys.maxsize,  nargs='?', help="Depth of Directories")
args = parser.parse_args()
visit("./", 0, args.depth)