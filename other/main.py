import sys
from parser import Parser

def main():
    if len(sys.argv) > 1:
        argv_idx = 1  # Index of file name in argv
        ast_flag = 0  # Flag to check if AST or ST is to be printed

        if len(sys.argv) == 3:  # Check if AST or ST flag is present
            argv_idx = 2
            if sys.argv[1] == "-ast":  # Check if AST flag is present
                ast_flag = 1
            elif sys.argv[1] == "-st":  # Check if ST flag is present
                ast_flag = 2

        filepath = sys.argv[argv_idx]  # Read file name from command line

        try:
            with open(filepath, 'r') as file:
                file_str = file.read()  # Read file into string
        except FileNotFoundError:
            print(f'File "{filepath}" not found!')
            return 1

        # Create parser object and start parsing
        rpal_parser = Parser(file_str, 0, len(file_str), ast_flag)
        rpal_parser.parse()
    else:
        print("Error: Incorrect number of inputs")

if __name__ == "__main__":
    main()