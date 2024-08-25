def print_node(self):
    print("<", end="")
    print(self.type, end="")
    print(":", end="")

    # If node type is BOOL, NIL or DUMMY, print <
    if self.type in ["BOOL", "NIL", "DUMMY"]:
        print("<", end="")

    print(self.val, end="")

    # If node type is ID, STR or INT, print >
    if self.type in ["ID", "STR", "INT"]:
        print(">", end="")

    # If node type is BOOL, NIL or DUMMY, print >
    if self.type in ["BOOL", "NIL", "DUMMY"]:
        print(">", end="")

    print()