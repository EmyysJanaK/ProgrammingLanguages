class Environment:
    def __init__(self):
        self.prev = None  # Pointer to the previous environment
        self.name = "env0"  # Default name
        self.boundVar = {}  # Map of bound variables to their values