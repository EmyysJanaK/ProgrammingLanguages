from enum import Enum
from lexical_analyzer.Token import Token
from lexical_analyzer.TokenType import TokenType

class TokenType(Enum):
    KEYWORD = 1
    IDENTIFIER = 2
    INTEGER = 3
    STRING = 4
    PUNCTUATION = 5
    EndOfTokens = 6

class NodeType(Enum):
    identifier = 1
    integer = 2
    string = 3
    true_value = 4
    false_value = 5
    nil = 6
    dummy = 7
    fcn_form = 8
    let = 9
    lambda_expr = 10
    tau = 11
    aug = 12
    conditional = 13
    op_or = 14
    op_and = 15
    op_not = 16
    op_compare = 17
    op_plus = 18
    op_minus = 19
    op_mul = 20
    op_div = 21
    op_pow = 22
    at = 23
    gamma = 24
    within = 25
    and_op = 26
    rec = 27
    equal = 28
    empty_params = 29
    comma = 30

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Node:
    def __init__(self, type, value, no_of_children):
        self.type = type
        self.value = value
        self.no_of_children = no_of_children

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.AST = []
        self.stringAST = []

    def parse(self):
        self.tokens.append(Token(TokenType.EndOfTokens, ""))
        self.E()
        if self.tokens[0].type == TokenType.EndOfTokens:
            print("ParsingSuccessful!...........")
            return self.AST
        else:
            print("Parsing Unsuccessful!...........")
            print("REMAINIG UNPARSED TOKENS:")
            for token in self.tokens:
                print("<" + token.type.name + ", " + token.value + ">")
            return None

    def convertAST_toStringAST(self):
        dots = ""
        stack = []
        
        while self.AST:
            if not stack:
                if self.AST[-1].no_of_children == 0:
                    self.addStrings(dots, self.AST.pop())
                else:
                    node = self.AST.pop()
                    stack.append(node)
            else:
                if self.AST[-1].no_of_children > 0:
                    node = self.AST.pop()
                    stack.append(node)
                    dots += "."
                else:
                    stack.append(self.AST.pop())
                    dots += "."
                    while stack[-1].no_of_children == 0:
                        self.addStrings(dots, stack.pop())
                        if not stack:
                            break
                        dots = dots[:-1]
                        node = stack.pop()
                        node.no_of_children -= 1
                        stack.append(node)

        self.stringAST.reverse()
        return self.stringAST

    def addStrings(self, dots, node):
        if node.type in [NodeType.identifier, NodeType.integer, NodeType.string, NodeType.true_value,
                         NodeType.false_value, NodeType.nil, NodeType.dummy]:
            self.stringAST.append(dots + "<" + node.type.name + ":" + node.value + ">")
        elif node.type == NodeType.fcn_form:
            self.stringAST.append(dots + "function_form")
        else:
            self.stringAST.append(dots + node.value)
